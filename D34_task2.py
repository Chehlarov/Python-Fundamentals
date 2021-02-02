import re

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

n = int(input())

for _ in range(n):
    barcode = input()
    if re.match(pattern, barcode):
        digits = re.findall(r"\d", barcode)
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
