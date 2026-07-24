from monitor import get_products
from database import check_updates
from discord_notify import (
    update_status,
    send_new_products,
    send_sale_changes
)
products = get_products()

new_products, sale_changes = check_updates(products)

print(f"官方商品：{len(products)}")
print(f"新增商品：{len(new_products)}")
print(f"開賣時間變動：{len(sale_changes)}")

update_status(products)

send_new_products(new_products)
send_sale_changes(sale_changes)
