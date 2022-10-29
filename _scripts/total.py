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

pence = int(out.split("totalValue")[1].split("£")[1].split("<")[0].replace(".", "").replace(",", ""))

if pence % 100 == 0:
    money = f"£{pence//100}"
else:
    money = f"£{pence//100}.{pad2(pence % 100)}"

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../_includes/_total.html"), "w") as f:
    f.write(money)


permille = pence * 1000 // 1000000

if permille % 10 == 0:
    percent = f"{permille // 10}%"
else:
    percent = f"{permille // 10}.{permille % 10}%"

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../_includes/_progress.html"), "w") as f:
    f.write("<div style='width:100%;border:2px solid black;height:40px'>")
    f.write(f"<div style='display:inline-block;width:{percent};background-color:#88C7D9;height:40px;line-height:40px;vertical-align:middle;text-align:right'>")
    if permille > 500:
        f.write(f"{percent} of £10,000 target&nbsp;")
    f.write("</div>")
    if permille <= 500:
        f.write(f"<div style='display:inline-block;height:40px;line-height:40px;vertical-align:middle'>")
        f.write(f"&nbsp;{percent} of £10,000 target")
        f.write("</div>")
    f.write("</div>")


with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../totaliser.md"), "w") as f:
    f.write("---\n")
    f.write("permalink: totaliser\n")
    f.write("layout: totaliser\n")
    f.write("---\n")

    if pence >= 314159 and pence < 330000:
        f.write("<div style='text-align:center;font-size:300%;padding-top:30px'>Money raised so far:</div>\n"
                f"<div style='font-weight:bold;text-align:center;font-size:400%'>£1000&pi;</div>\n")
    else:
        f.write("<div style='text-align:center;font-size:300%;padding-top:30px'>Money raised so far:</div>\n"
                f"<div style='font-weight:bold;text-align:center;font-size:400%'>{money}</div>\n")
