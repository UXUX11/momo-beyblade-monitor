import json
import requests

SEARCH_URL = "https://www.momoshop.com.tw/search/searchShop.jsp?keyword=%E6%88%B0%E9%AC%A5%E9%99%80%E8%9E%BA%20X"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}


def download_page():
    r = requests.get(
        SEARCH_URL,
        headers=HEADERS,
        timeout=30
    )
    r.raise_for_status()
    return r.text





def extract_goods_list(html: str):

    idx = html.find("goodsInfoList")

    if idx == -1:
        raise Exception("找不到 goodsInfoList")

    start = html.find("[", idx)

    if start == -1:
        raise Exception("找不到 goodsInfoList [")

    depth = 0
    in_string = False
    escape = False

    for i in range(start, len(html)):

        c = html[i]

        if escape:
            escape = False
            continue

        if c == "\\":
            escape = True
            continue

        if c == '"':
            in_string = not in_string
            continue

        if in_string:
            continue

        if c == "[":
            depth += 1

        elif c == "]":
            depth -= 1

            if depth == 0:

                array_text = html[start:i+1]

                # Next.js 會把 JSON 轉義
                array_text = (
                array_text
                    .replace(r"\/", "/")
                    .replace(r"\"", '"')
                )
                return json.loads(array_text)

    raise Exception("goodsInfoList 結束位置找不到")


def official_goods(goods_list):

    result = []

    for g in goods_list:

        code = str(g.get("goodsCode", ""))

        if code.startswith("TP"):
            continue

        result.append({
            "code": code,
            "name": g.get("goodsName", ""),
            "price": g.get("SALE_PRICE", ""),
            "stock": g.get("goodsStock", ""),
            "sale": g.get("onSaleDescription", ""),
            "url": g.get("goodsUrl", ""),
            "image": g.get("imgUrl", "")
        })

    return result


def get_products():

    html = download_page()

    goods = extract_goods_list(html)

    return official_goods(goods)


def main():

    products = get_products()

    print(f"官方商品：{len(products)}")

    for p in products:

        print("=" * 60)
        print(p["code"])
        print(p["name"])
        print("價格 :", p["price"])
        print("庫存 :", p["stock"])
        print("開賣 :", p["sale"])


if __name__ == "__main__":
    main()