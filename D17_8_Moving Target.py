targets = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "Shoot":
        i = int(command[1])
        power = int(command[2])
        if 0 <= i < len(targets):
            targets[i] -= power
            if targets[i] <= 0:
                targets.pop(i)
    elif command[0] == "Add":
        i = int(command[1])
        value = int(command[2])
        if 0 <= i < len(targets):
            targets.insert(i, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        i = int(command[1])
        radius = int(command[2])
        if 0 <= i - radius and i + radius < len(targets):
            # for j in range(i - radius, i + radius):
            #     targets.pop(j)
            # targets[i-radius:i+radius].pop()
            left = targets[:i - radius]
            right = targets[i + radius + 1:]
            targets = left + right
        else:
            print("Strike missed!")

out = '|'.join([str(el) for el in targets])
print(out)
