import rooms
import player
current_room = rooms.room5()
user = player.Player()

def pickup_item(input_item):
    global current_room
    global user
    line_value = current_room.room_name()

    with open('inventory.txt', 'r') as file:
        data = file.readlines()

    current_inventory = str(data[line_value-1])
    if input_item in current_inventory:
        new_inventory = current_inventory.replace(input_item, "")
        data[line_value-1] = new_inventory
        user.inventory.append(input_item)
        print(user.inventory)

        with open('inventory.txt', 'w') as file:
            file.writelines(data)

        file.close()
    elif input_item == "c":
        return None
    else:
        print("That item isn't in this room sorry!")
        item = input("Please input an item to pick up")
        pickup_item(item)
pickup_item("car")









def drop_item(input_item):
    global current_room
    global user
    try:
        if input_item == "c":
            return None
        elif input_item in user.inventory == True:
                current_room.items.append(input_item)
                user.inventory.remove(input_item)
                print("You have dropped " + input_item)

        else:
            print("You cannot drop that item!")
            item_input = str(input("Please enter an item to drop:")).lower()
            input_item = item_input.split(" ")
            drop_item(input_item[0])
    except ValueError:
        print("That is not a recognised value!")

    print(user.inventory)
