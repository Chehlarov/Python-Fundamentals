def factorial(n: int):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


a = int(input())
b = int(input())
print(f"{factorial(a) / factorial(b):.2f}")
