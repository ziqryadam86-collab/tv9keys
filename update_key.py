import requests
import re

url = "https://buttoncalc.blogspot.com/2026/06/photo.html?m=1"

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html = response.text

    # 1. Kita cari blok pembungkus saluran (channel-item) yang mengandungi TV9
    # Kita scan setiap ketul <li>...</li> sampai jumpa yang ada tulisan TV9
    channels = re.findall(r'<li class="channel-item">.*?</li>', html, re.DOTALL)
    
    tv9_html = None
    for channel in channels:
        if 'alt="TV9"' in channel or 'class="channel-name">TV9</span>' in channel:
            tv9_html = channel
            break

    if tv9_html:
        # 2. Sekarang kita scan KID dan KEY dalam blok TV9 yang tepat ini sahaja!
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
            print("Kunci dalam blok TV9 tidak dijumpai!")
    else:
        print("Gagal menjumpai siaran TV9 dalam HTML!")

except Exception as e:
    print(f"Ralat: {e}")
    
