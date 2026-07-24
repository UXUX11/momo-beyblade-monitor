import os
import requests

from config import WEBHOOK_URL, MESSAGE_ID_FILE
from line_notify import send_line

def send_new_products(products):
    if not products:
        return

    for p in products:
        message = (
            "🆕 **MOMO 新商品**\n\n"
            f"**{p['name']}**\n\n"
            f"💰 價格：{p['price']}\n"
            f"📦 庫存：{p['stock']}\n"
            f"🕒 開賣：{p['sale']}\n\n"
            f"{p['url']}"
        )

        requests.post(
            WEBHOOK_URL,
            json={"content": message},
            timeout=30,
        )
<<<<<<< HEAD
=======
        send_line(message)
def send_sale_changes(changes):
>>>>>>> 549d44f (Add LINE notifications)


def send_sale_changes(changes):
    if not changes:
        return

    for item in changes:
        p = item["product"]

        message = (
            "⏰ **MOMO 開賣時間更新**\n\n"
            f"**{p['name']}**\n\n"
            f"原本：{item['old_sale']}\n"
            f"現在：{item['new_sale']}\n\n"
            f"{p['url']}"
        )

        requests.post(
            WEBHOOK_URL,
            json={"content": message},
<<<<<<< HEAD
            timeout=30,
        )
=======
            timeout=30
        )        
        send_line(message)
def load_message_id():
>>>>>>> 549d44f (Add LINE notifications)


def load_message_id():
    if not os.path.exists(MESSAGE_ID_FILE):
        return None

    with open(MESSAGE_ID_FILE, "r") as f:
        return f.read().strip()


def save_message_id(message_id):
    with open(MESSAGE_ID_FILE, "w") as f:
        f.write(message_id)


def update_status(products):
    products = sorted(products, key=lambda x: x["sale"])

    lines = []
    lines.append("📦 **MOMO 官方商品**\n")

    for p in products:
        lines.append(
            f"**{p['name']}**\n"
            f"💰 售價：{p['price']} 元\n"
            f"📦 庫存：{p['stock']}\n"
            f"🕒 開賣：{p['sale']}\n"
            f"🛒 商品頁：{p['url']}\n"
        )

    content = "\n".join(lines)

    message_id = load_message_id()

    if message_id is None:
        r = requests.post(
            WEBHOOK_URL + "?wait=true",
            json={"content": content},
            timeout=30,
        )

        r.raise_for_status()
        save_message_id(r.json()["id"])
        return

    r = requests.patch(
        WEBHOOK_URL + f"/messages/{message_id}",
        json={"content": content},
        timeout=30,
    )

    if r.status_code == 404:
        os.remove(MESSAGE_ID_FILE)
        update_status(products)
        return

    r.raise_for_status()