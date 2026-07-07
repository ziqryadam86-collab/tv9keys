import requests
import re

url = "https://buttoncalc.blogspot.com/2026/06/photo.html?m=1"

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html = response.text

    # 1. Kita potong HTML tu, ambil bahagian TV9 sahaja
    # Kita cari text yang ada 'alt="TV9"' sampai lah '</span>'
    tv9_section = re.search(r'alt="TV9".*?</span>', html, re.DOTALL)

    if tv9_section:
        tv9_html = tv9_section.group(0)
        
        # 2. Baru kita scan KID dan KEY dalam bahagian TV9 tadi sahaja
        kid_match = re.search(r'kid&quot;:&quot;([a-f0-9]{32})&quot;', tv9_html)
        key_match = re.search(r'key&quot;:&quot;([a-f0-9]{32})&quot;', tv9_html)

        if kid_match and key_match:
            kid = kid_match.group(1)
            key = key_match.group(1)
            
            # Simpan dalam fail keys.txt
            with open("keys.txt", "w") as f:
                f.write(f"{kid}:{key}")
            print(f"Berjaya dapatkan Kunci TV9: {kid}:{key}")
        else:
            print("Kunci dalam section TV9 tidak dijumpai!")
    else:
        print("Gagal menjumpai siaran TV9 dalam HTML!")

except Exception as e:
    print(f"Ralat: {e}")
    
