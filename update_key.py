import requests
import re

# URL Blogspot abang
url = "https://buttoncalc.blogspot.com/2026/06/photo.html?m=1"

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html = response.text

    # Regex untuk picit KID dan KEY
    kid_match = re.search(r'kid&quot;:&quot;([a-f0-9]{32})&quot;', html)
    key_match = re.search(r'key&quot;:&quot;([a-f0-9]{32})&quot;', html)

    if kid_match and key_match:
        kid = kid_match.group(1)
        key = key_match.group(1)
        
        # Simpan format KID:KEY dalam fail
        with open("keys.txt", "w") as f:
            f.write(f"{kid}:{key}")
        print(f"Update Berjaya: {kid}:{key}")
    else:
        print("Gagal jumpa kunci dalam HTML!")
except Exception as e:
    print(f"Ralat: {e}")
                  
