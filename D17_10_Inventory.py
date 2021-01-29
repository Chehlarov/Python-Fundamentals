items = input().split()

data = input()


def collect_item(items_list, i):
    if i not in items_list:
        items_list.append(i)
    return items_list


def drop_item(item_list, i):
    if i in item_list:
        item_list.remove(i)
    return item_list


def combine_item(item_lists: list, i):
    old_item = i.split(":")[0]
    new_item = i.split(":")[1]
    if old_item in item_lists:
        index_old_item = item_lists.index(old_item)
        index_new_item = index_old_item + 1
        item_lists.insert(index_new_item, new_item)
    return item_lists


def renew_items(item_list, i):
    if i in item_list:
        item_list.remove(i)
        item_list.append(i)
    return item_list


while not data == "Craft!":
    command, item = data.split(" - ")
    if command == "Collect":
        items = collect_item(items, item)
    elif command == "Drop":
        items = drop_item(items, item)
    elif command == "Combine Items":
        items = combine_item(items, item)
    elif command == "Renew":
        items = renew_items(items, item)

    data = input()

print(", ".join(items))
