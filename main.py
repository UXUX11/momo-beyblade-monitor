from monitor import get_products
from database import (
    check_updates,
    load_database,
    need_daily_summary,
    mark_daily_summary,
)
from discord_notify import (
    update_status,
    send_new_products,
    send_sale_changes,
    send_daily_summary,
)
from datetime import datetime
products = get_products()

new_products, sale_changes = check_updates(products)

print(f"官方商品：{len(products)}")
print(f"新增商品：{len(new_products)}")
print(f"開賣時間變動：{len(sale_changes)}")

update_status(products)

send_new_products(new_products)
send_sale_changes(sale_changes)

# 每日09:00 LINE摘要
now = datetime.now()

if now.hour == 9 and now.minute < 15:

    db = load_database()

    if need_daily_summary(db):
        send_daily_summary(products)
        mark_daily_summary(db)