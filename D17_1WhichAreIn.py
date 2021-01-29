substrings = input().split(", ")
words = input().split(", ")

# result = [el for el in substrings if el in ]

result = [subst for subst in substrings for word in words if subst in word]
# unique = [el for el in result if el not in unique]


print(sorted(set(result), key=result.index))
