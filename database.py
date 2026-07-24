import json
import os
from datetime import date

DB_FILE = "known_products.json"


def load_database():

    if not os.path.exists(DB_FILE):
        return {}

    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_database(data):

    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


def check_updates(products):

    db = load_database()

    # 第一次執行
    if not db:

        for p in products:
            db[p["code"]] = p
            db["last_daily_summary"] = ""

        save_database(db)

        return [], []

    new_products = []
    sale_changes = []

    for p in products:

        code = p["code"]

        # 新商品
        if code not in db:

            new_products.append(p)
            db[code] = p
            continue

        # 開賣時間改變
        if db[code]["sale"] != p["sale"]:

            sale_changes.append({
                "product": p,
                "old_sale": db[code]["sale"],
                "new_sale": p["sale"]
            })

            db[code]["sale"] = p["sale"]

    save_database(db)

    return new_products, sale_changes



def need_daily_summary(db):
    today = date.today().isoformat()
    return db.get("last_daily_summary", "") != today


def mark_daily_summary(db):
    db["last_daily_summary"] = date.today().isoformat()
    save_database(db)