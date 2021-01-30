data = input()

result = data[0]

for i in range(len(data)):
    if result[-1] != data[i]:
        result = result + data[i]

print(result)