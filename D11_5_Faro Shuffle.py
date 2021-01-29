cards = input().split(" ")
number_of_shuffle = int(input())
mid = int(len(cards) * 0.5)
processed_cards = []

for i in range(number_of_shuffle):
    for j in range(0, mid):
        processed_cards.append(cards[j])
        processed_cards.append(cards[j + mid])
    cards = processed_cards.copy()  # strange but works well even without copy
    processed_cards = []

print(cards)
