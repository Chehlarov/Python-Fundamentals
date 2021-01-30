product_prices = {}
product_qty = {}

while True:
    data = input()
    if data == "buy":
        break

    product, price, qty = data.split()
    price = float(price)
    qty = int(qty)
    if product in product_prices:
        product_prices[product] = price
        product_qty[product] += qty
    else:
        product_prices[product] = price
        product_qty[product] = qty

for product in product_prices:
    print(f"{product} -> {product_prices[product] * product_qty[product]:.2f}")
