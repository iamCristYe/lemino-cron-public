import requests
import os
import json
import time
import requests


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
        if no > 10:
            sendTelegramMsg("lemino!!")
        break
    except Exception as e:
        sendTelegramMsg(e)
        break
