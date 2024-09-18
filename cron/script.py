import requests
import os
import json
import time
import requests
import string
import json
import requests
import subprocess

base = ""
for i in range(0, 10):
    base += str(i)
base += string.ascii_lowercase
# print(len(base))


def decode(str):
    ls = list(str)
    result = 0
    for i in range(len(ls)):
        current = ls[-1 - i]
        num = base.index(current)
        result += pow(36, i) * num
    return result


def encode(num):
    result = []
    while num >= 36:
        remainder = num % 36
        import math

        num = math.floor((num - remainder) / 36)
        result.append(base[remainder])

    result.append(base[num])
    res = ""
    for i in range(len(result)):
        res += result[-1 - i]
    return str(res)


def sendTelegramMsg(message):
    # Replace with your own bot token and chat ID
    bot_token = os.environ["bot_token"]
    chat_id = os.environ["chat_id"]
    # message = "Hello, this is a test message from Python!"

    # Telegram API URL
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # Payload to send the message
    payload = {"chat_id": chat_id, "text": message}

    # Send the request
    requests.post(url, data=payload)


while True:
    try:
        result = json.loads(requests.get(os.environ["URL"]).content)
        no = len(result["meta_list"][0]["child_license_list"])
        # sendTelegramMsg(f"lemino EP{no}")
        print(no)
        if no > 12:
            sendTelegramMsg("leminoN")
            break
    except Exception as e:
        sendTelegramMsg(e)
        break
while True:
    try:
        result = json.loads(requests.get(os.environ["URL_S"]).content)
        no = len(result["meta_list"][0]["child_license_list"])
        # sendTelegramMsg(f"lemino EP{no}")
        print(no)
        if no > 12:
            sendTelegramMsg("leminoS")
            break
    except Exception as e:
        sendTelegramMsg(e)
        break


init = decode("00lx311r65")

for i in range(920, 1100):
    cid = f"00{encode(init+i)}"
    print(i, cid)
    url = f"https://vod-cdn0.lemino.docomo.ne.jp/img/{cid}/thumbnail/0250.jpg"
    print(url)
    # response = requests.head(url)

    # # Get content size in bytes
    # content_size = int(response.headers.get("Content-Length", 0))

    # # Check if the content size is greater than 2KB (2048 bytes)
    # if content_size > 2048:
    #     print(url)
    #     break
    # else:
    #     print("Size is smaller than 2KB, not saved.")
