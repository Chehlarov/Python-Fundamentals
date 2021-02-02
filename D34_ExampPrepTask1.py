def take_odd(password):
    result = ""
    for i in range(1, len(password), 2):
        result += password[i]
    print(result)
    return result


def cut(password, i, length):
    result = password[:i] + password[i + length:]
    print(result)
    return result


def substitude(password, sub_str, replacement):
    result = password.replace(sub_str, replacement)
    if result == password:
        print("Nothing to replace!")
    else:
        print(result)
    return result

password = input()
while True:
    line = input()
    if line == "Done":
        break
    data = line.split()
    command = data[0]
    if command == "TakeOdd":
        password = take_odd(password)
    elif command == "Cut":
        index, length = [int(el) for el in data[1:]]
        password = cut(password, index, length)
    elif command == "Substitute":
        sub_str, replacement = [el for el in data[1:]]
        password = substitude(password, sub_str, replacement)

print(f"Your password is: {password}")
