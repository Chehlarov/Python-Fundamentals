# import re
#
# data = input()
# pattern = r"\+359\s2\s\d{3}\s\d{4}\b"
# phones = re.finditer(pattern, data)
# phones = [p.group(0) for p in phones]
# print(', '.join(phones))

#task 3
import re

# data = input()
# pattern = r"(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
# dates = re.finditer(pattern, data)
# for d in dates:
#     res = d.groupdict()
#     print(f"Day: {d['day']}, Month: {d['month']}, Year: {d['year']}")

#task 4
import re

data = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
nums = re.finditer(pattern, data)
nums = [n.group() for n in nums]
print(*nums)


