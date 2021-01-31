import re
pattern = r"\d+"
nums = []
while True:
    data = input()
    if data == "":
        break
    match = re.findall(pattern, data)
    if match:
        nums.extend(match)

print(*nums, sep=" ")
