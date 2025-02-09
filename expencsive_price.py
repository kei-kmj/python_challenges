

# あなたは、複数の商品のリストを与えられます。各商品は 名前と価格 で表されます。
# このリストから N番目に高価な商品 の名前を出力してください。
# ただし、同じ価格の商品が複数ある場合は、辞書順（アルファベット順）で最も早い商品を選びます。


products = [
    ["Laptop", 1500],
    ["Smartphone", 900],
    ["Tablet", 500],
    ["Smartwatch", 200],
    ["Desktop", 1500],
    ["Monitor", 700]
]
N = 2


def find_nth_expensive_product(products, N):
    sorted_products = sorted(products, key=lambda product: (lambda price, name: (-price, name))(*product))

    return sorted_products[N-1][0]


print(find_nth_expensive_product(products, N))