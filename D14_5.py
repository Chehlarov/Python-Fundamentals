def is_palindrome(element, ):
    if element == element[::-1]:
        return True
    return False


strings = input().split(", ")
for el in strings:
    print(is_palindrome(str(el)))
