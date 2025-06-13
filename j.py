import requests
import time
import os
from datetime import datetime

def auto_start_mining(uid, lang):
    url = "https://keycloudapi.com/Go/_Start_ClickToStart"
    payload = {
        'uid': uid,
        'langu': lang
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'x-request-id': "1749783279095",
        'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlMTFhYzZhOTM4ZjU0MGNhYWE3MWVjY2EzZjU5MTdhNyIsImp0aSI6IjU4YTRjMGJkLTEzOGMtNDIzYy04ZTcxLTcyYmJmOTdlM2Y3NiIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWUiOiJlMTFhYzZhOTM4ZjU0MGNhYWE3MWVjY2EzZjU5MTdhNyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IlVzZXIiLCJleHAiOjE3NDk3ODQxNjAsImlzcyI6IkRELVNlcnZlciIsImF1ZCI6IkQtSU0ifQ.eLk6dKwoGQFwuYa1rsbbMKN_3nAuvZx2e37O32fL_MA",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Chromium\";v=\"130\", \"Mises\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
        'sec-ch-ua-mobile': "?1",
        'origin': "https://www.key.top",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.key.top/",
        'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        'priority': "u=1, i"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        return response.json()  # Assume the response is in JSON format
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except Exception as err:
        return f"An error occurred: {err}"

def has_claimed_today():
    if os.path.exists("last_claim.txt"):
        with open("last_claim.txt", "r") as file:
            last_claim_date = file.read().strip()
            today_date = datetime.now().strftime("%Y-%m-%d")
            return last_claim_date == today_date
    return False

def mark_claimed_today():
    today_date = datetime.now().strftime("%Y-%m-%d")
    with open("last_claim.txt", "w") as file:
        file.write(today_date)

# Main loop
uid = "e11ac6a938f540caaa71ecca3f5917a7"
lang = "en"

while True:
    if not has_claimed_today():
        result = auto_start_mining(uid, lang)
        print(result)
        mark_claimed_today()  # Tandai bahwa klaim telah dilakukan hari ini
    else:
        print("Anda sudah melakukan klaim hari ini. Tunggu sampai besok.")

    # Tunggu selama 1 jam (3600 detik) sebelum pengecekan berikutnya
    time.sleep(3600)
