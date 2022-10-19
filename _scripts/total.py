import json
import requests
import os


def pad2(n):
    out = str(n)
    while len(out) < 2:
        out = "0" + out
    return out


url = "https://www.justgiving.com/team/24hourmathsgameshow"
headers = {}
cookies = {}
headers["User-Agent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/50.0.2661.102 Safari/537.36")
out = requests.get(url, headers=headers, cookies=cookies).text

pence = int(out.split("totalValue")[1].split("£")[1].split("<")[0].replace(".", ""))

money = f"£{pence//100}.{pad2(pence % 100)}"

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../_includes/_total.html"), "w") as f:
    f.write(money)
