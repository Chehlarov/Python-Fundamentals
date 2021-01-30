words = input().split()
first_w = words[0]
second_w = words[1]

min_length = min(len(first_w), len(second_w))
total_sum = 0

for i in range(min_length):
    total_sum += ord(first_w[i]) * ord(second_w[i])

if len(first_w) > len(second_w):
    res = first_w[min_length:]
else:
    res = second_w[min_length:]

total_sum += sum([ord(x) for x in res])

print(total_sum)