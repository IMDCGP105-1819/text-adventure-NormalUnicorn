import rooms
import player
current_room = rooms.room5()
user = player.Player()

def pickup_item(input_item):
    global current_room
    global user
    line_value = current_room.room_name()
    current_inventory = []
    with open('inventory.txt', 'r') as file:
        data = file.readlines()
    print(data)
    data[1] = "text\n"
    print(data)
    with open('inventory.txt', 'w') as file:
        file.writelines(data)





pickup_item(None)









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
