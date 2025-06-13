import requests
import time
from colorama import Fore, Style, init
import json

# Inisialisasi colorama
init(autoreset=True)

# Fungsi untuk melakukan klaim
def claim():
    url = "https://keycloudapi.com/Go/_Start_ClickToStart"

    # Ganti dengan akun baru
    payload = {
        'uid': "7023b9f2d2c742d79c1817e8cccf1e33",  # UID baru
        'langu': "en"  # Mengganti 'laugh' menjadi 'langu'
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'x-request-id': "1749478220501",
        'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI3MDIzYjlmMmQyYzc0MmQ3OWMxODE3ZThjY2NmMWUzMyIsImp0aSI6ImMzMWE1MDhjLTdhNmItNDZmOS04MzYyLThkZmU5YjQyOWE3ZSIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWUiOiI3MDIzYjlmMmQyYzc0MmQ3OWMxODE3ZThjY2NmMWUzMyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlVzZXIiLCJleHAiOjE3NDk0NzkxMTksImlzcyI6IkRELVNlcnZlciIsImF1ZCI6IkQtSU0ifQ.SEQtyTBftydPHyp4QTXY8e1dyupmR-QLD-A-zA3Q5jo",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        'sec-ch-ua-mobile': "?1",
        'origin': "https://www.key.top",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.key.top/",
        'accept-language': "id,en-US;q=0.9,en;q=0.8,jv;q=0.7,zh-CN;q=0.6,zh;q=0.5",
        'priority': "u=1, i"
    }

    # Melakukan permintaan POST
    response = requests.post(url, data=payload, headers=headers)
    
    # Memeriksa status code
    if response.status_code == 200:
        print(Fore.GREEN + "Claim berhasil.")
        try:
            data = response.json()  # Mengambil respon dalam format JSON
            print(Fore.LIGHTCYAN_EX + json.dumps(data, indent=4))
            print(Fore.LIGHTCYAN_EX + f"State: {data['State']}, Result: {data['Result']}, Message: {data['Msg']}")
        except ValueError:
            print(Fore.YELLOW + "Respon bukan dalam format JSON.")
            print(Fore.LIGHTCYAN_EX + response.text)
    else:
        print(Fore.RED + "Terjadi kesalahan saat mengklaim!")
        print(Fore.LIGHTRED_EX + f"Status Code: {response.status_code}")
        print(Fore.LIGHTRED_EX + response.text)

# Memulai loop klaim yang terus menerus
while True:
    print(Fore.YELLOW + "Menunggu selama 24 jam sebelum melakukan klaim...")
    time.sleep(86400)  # Tunggu selama 24 jam sebelum melakukan klaim
    claim()  # Melakukan klaim setelah penundaan
