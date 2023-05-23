import requests
from bs4 import BeautifulSoup
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

usernames = {"rutshelle","bedjineofficiel","tafaayiti","darlinedesca","blondedyferdinandshop","fatiful","aniealerte","vanessa_desireofficiel"}
url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"

sender_email = "lamourjoud09@gmail.com"
receiver_email = "esih.license@gmail.com"
password = "sdxhskwomjbxnojz"

message = MIMEMultipart("alternative")
message["Subject"] = datetime.now().strftime('%Y-%m-%d %H:%M')
message["From"] = sender_email
message["To"] = receiver_email

text = """\
"""

for username in usernames:
    link = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
    file_name = "Total_Abonnees.txt"
    headers = {
        "authority": "www.instagram.com",
        "method": "GET",
        "path": "/api/v1/users/web_profile_info/?username=bedjineofficiel",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie":'mid=YlePQQALAAFZ-xe9LVYboc85D27D; ig_did=011151DE-A958-45D8-920C-8251D5DAADA7; datr=LKu_YoL3zzKkDzntzsd63EOJ; ig_nrcb=1; dpr=1.5; fbm_124024574287414=base_domain=.instagram.com; csrftoken=Y4fUdNXOuVjE7y5S6sDDM0eQgcXp22SK; ds_user_id=8375204440; sessionid=8375204440%3ARYIg5gvCf4fghs%3A12%3AAYcaIJv50Hh2I_wP5FHixTvQqheZG5zNv-dk7YPd0g; shbid="12518\0548375204440\0541713728937:01f78af6dc7494232918acce52d781cdfa5a1db51feba2b6e85017cf11b223a2fd90fd3b"; shbts="1682192937\0548375204440\0541713728937:01f707e1e2b2a41e12c87f5c19ce50330928f7dc3229281502fa75086545dcfe86343b43"; fbsr_124024574287414=mG85P_HCraqOGGwcErBBmaK1RITnof1IWCZWpVlfq0k.eyJ1c2VyX2lkIjoiMTAwMDU1NjA2Nzc2MjgzIiwiY29kZSI6IkFRREV0dEpxMEFieDF6UUQxd0pLZFVXSGppMVNvTlRoVFRqR2NaWTJpQV9JRDNiZmVQNlEyY053cWtwNTByWlYyaS0tRnhnR0l5Nl9wbkl6RXlUZ2o3ZExTNlFjb1dVVzZIaGF5bHQ4MnpsZzVGNk5sRmg4dGlFZGRaTjJvb0lpVTBjLU9Od3l2azVWMXpBVnVTdlRONjNxdDZvLXJnRFB3dEdrMjBlWk1NUDQ1XzNLcEpLRFRuYm5SZXVnSGlOdXJPdmxEdXh6bm5GNXpXT2hHX3hjbXdhVHB0bmUtd01DeWhvRUFxY1NIaVoza0EyUFRHWWtwQ1F4aVpEZ0JxWUUzaTVLTXdiX0RubklERWtqVDByckV2OG9jZmhNV3NkT1drRmdmRlBfeXI4U0cyUFF0Q1FNcXR3cmJJX0Z3QzBjQVBoNVp4YzdGNHVSOGVfcE9oOG5EaF9qIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU1kUE1uUlNBN0ZaQXhyZkVlbzRUUFZ2MTNTQUhpUlRTbmJxdVI4ZTFNdkpjOENZbUl5TzBWWkFGTXFwYUl4NDlRWkJOeEhicXlsQlF3aVpBM1pCODRhQ3RpUE1TY3daQlBmWElHbFQ4TUE4VW9nMVVaQnlZZlpDWXByM2xaQTBVQ0R0NnV3SXZiVUVsdHJBdWRNTTVZU0tvWkN0bGpsMlpCS281MzhxWkNPNGpsYTdlMW9PenNKWGcxc1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODIxOTQ5MzF9; fbsr_124024574287414=O9JXIrtYkO4bh4tybKX_1pc5ypatjr6h-53JxOtSWR0.eyJ1c2VyX2lkIjoiMTAwMDU1NjA2Nzc2MjgzIiwiY29kZSI6IkFRQk5aM18wa190LW90cmRJeHBZeXBwSGNuZEFzRnllVk5udUdXdWY5enBEaXZaMi1tcHd5SjB2NlNiWWotZ0ppOThRVTRDMFh0U3RSaWtIVzRTaUsxazBtcUNEVTNTOXl6ZS0xVk9hTmZ3MmxPWFVBQXpwaWwxOElyYTU3WFI5YnhtcHFiVFlmdXllVHNSR3NkTGdfbFdMcFoyS3ZKcmdPcHpDdTJPQUZxTkVLOXpEMXF3blV3cl9URHFRRjg3VEhWY2NxUE1uc21UUkdOQTFOamVQdGNqdzV1VXYtY3hTeXZRQ3ZaVzJKaWtQdXZOTGEwbE01YnRqZVhpRXFYb1FNQXRaVjhxYnJVb0pTWV9LaU8yc3hrNEt4eDdlVW1yQ3JtTmM1RUNwMFA5X01zQUVPZnVlWDBEMmdEbTg5MXIxbXpUTGVGZmVCRHpuT1QwRmpuWHQtRXp0Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQVA1eUxwamFQa3BFWkJkUm5Rc1JrSVpBcFRUeDJzc21CSWlnQ2JCQXlFVEoyZDBaQ0tCTnRBUzFCRTUwNktVa0ZRTlF2TFpCSkhVS2NycG5zdkIxcnRrOVdwWkN1V2tQazRIRG5uUURXMjl4U0RnT0liOEp5ekpVeHZaQ1pBMlVLWkJhdlpCcnh1OW5Uc2g2M2k1YXpjcVFZY0FDeWI5TUE0Q0ZDOHJINDVkWWdKNmhsWHppRWU1Y1pEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2ODIxOTYyODN9; rur="NCG\0548375204440\0541713732318:01f79592f563065395203380c5a20c18c71567800721c8682d35c7a6104ad812f4d83ae7"',
        "referer": f"https://www.instagram.com/{username}/",
        "sec-ch-prefers-color-scheme": "light",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "viewport-width": "892",
        "x-asbd-id": "198387",
        "x-csrftoken": "ClQLdIbKjvQFM2jjWapCrH8gfHMaJZg3",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "hmac.AR3yHcUmXLFtk5CFSgHQ0wAv-1XtoJydd2JQFdj0hs0NoQ7c"
    }
    website = requests.get(url)

    proxybs = BeautifulSoup(website.content,"html.parser")

    proxylist = proxybs.get_text().strip().split("\n")
    while True:
        proxy = random.choice(proxylist)
        try:
            res = requests.get(link,headers = headers,proxies={"http":proxy},timeout=5)
            if res.status_code == 200:
                web = res.json()
                followers = web["data"]["user"]["edge_followed_by"]["count"]
                follow = web["data"]["user"]["edge_follow"]["count"]
                text = text + f"\n Le compte instagram de {username} a {followers} abonnees et elle suit {follow} comptes."
                break
        except :
            pass
part1 = MIMEText(text,"plain")
message.attach(part1)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )