import requests
from config import LINE_CHANNEL_ACCESS_TOKEN

USER_ID = "U2e156da7b872114a21c02277a46bd7a7"

def send_line(message):
    headers = {
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "to": USER_ID,
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

    r = requests.post(
        "https://api.line.me/v2/bot/message/push",
        headers=headers,
        json=payload,
        timeout=30,
    )

    r.raise_for_status()