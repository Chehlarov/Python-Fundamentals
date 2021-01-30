data = input().split()
positions = {chr(ele + 97): ele + 1 for ele in range(26)}
result = 0

for el in data:
    first = el[0]
    last = el[-1]
    num = int(el[1:-1])
    if first.isupper():
        num /= positions[first.lower()]
    else:
        num *= positions[first.lower()]

    if last.isupper():
        num -= positions[last.lower()]
    else:
        num += positions[last.lower()]

    result += num

print(f"{float(result):.2f}")
