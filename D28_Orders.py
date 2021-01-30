class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty


products = []
while True:
    data = input()
    if data == "buy":
        break
    name, price, qty = data.split()
    price = float(price)
    qty = float(qty)
    if name in map(lambda x: x.name, products):
        product = list(filter(lambda x: x.name == name, products))[0]
        product.price = price
        product.qty += qty
    else:
        product = Product(name, price, qty)
        products.append(product)

for product in products:
    print(f"{product.name} -> {product.price * product.qty:.2f}")
