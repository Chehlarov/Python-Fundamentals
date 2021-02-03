n = int(input())
pieces = {}

for _ in range(n):
    line = input().split("|")
    pieces[line[0]] = {'composer': line[1], 'key': line[2]}

while True:
    data = input()
    if data == "Stop":
        break
    splitted_data = data.split('|')
    command = splitted_data[0]
    if command == "Add":
        piece, composer, key = splitted_data[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command == "Remove":
        piece = splitted_data[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == "ChangeKey":
        piece = splitted_data[1]
        new_key = splitted_data[2]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1]['composer']))

# for el in sorted_pieces:
#     print(f"{el[0]} -> Composer: {el[1]['composer']}, Key: {el[1]['key']}")

for piece, val in sorted_pieces:
    print(f"{piece} -> Composer: {val['composer']}, Key: {val['key']}")