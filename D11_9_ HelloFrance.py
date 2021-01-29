items = input().split("|")
budget = float(input())
bouht_items = []
overall_profit = 0

for item in items:
    item_type, item_price = item.split("->")
    item_price = float(item_price)
    if item_type == "Clothes" and item_price > 50:
        continue
    elif item_type == "Shoes" and item_price > 35:
        continue
    elif item_type == "Accessories" and item_price > 20.50:
        continue

    if budget >= item_price:
        budget -= item_price
        overall_profit += item_price * 0.4
        bouht_items.append(item_price * 1.4)

# print(bouht_items)
available_money = sum(bouht_items) + budget
for el in bouht_items:
    print(f"{el:.2f} ", end='')
print()
print(f"Profit: {overall_profit:.2f}")

if available_money >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
