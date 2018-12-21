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
        item = input("Please input an item to pick up: ")
        pickup_item(item)



def drop_item(input_item):
    global current_room
    global user
    line_value = current_room.room_name()-1
    if input_item in user.inventory:
        with open('inventory.txt', 'r') as file:
            inventory = file.readlines()

        current_inventory = str(inventory[line_value])
        new_inventory = input_item + ", " + current_inventory
        inventory[line_value] = new_inventory
        user.inventory.remove(input_item)
        with open('inventory.txt', 'w') as file:
            file.writelines(inventory)

        print(user.inventory)
    elif input_item == "c":
        return None
    else:
        print("You do not have that item to drop!")
        item = input("Please input an item to drop: ")
        drop_item(item)


drop_item("car")
