import re

line = input()
pattern = r"(?<=\s_)[A-Za-z0-9]+(?=[\s\.])"

res = re.findall(pattern, line)

print(res )