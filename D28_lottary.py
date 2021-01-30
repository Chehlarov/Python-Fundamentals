#not finished

tickets = input().split(", ")
data = [el.strip() for el in tickets]
# data2 = [el for el in tickets if len(el) == 20]
winning = ['@', '$', '#', '^']


def jackpot(t):
    pass


for t in data:
    if len(t) != 20:
        print("Invalid ticket")
        continue
    left = data[0:10]
    right = data[10:0]
    jack = 0
    for w in winning:
        if w*10 == left:
            jack += 1
        if w*10 == right:
            jack += 1
    if jack == 2:
        print("Jackpot")
