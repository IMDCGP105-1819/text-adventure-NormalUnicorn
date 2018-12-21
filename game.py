import rooms
import player

# Create an instance of the room class that the player is in
current_room = rooms.room5()
user = player.Player()
choice = ""


def move(direction):
    """
    The function move works by taking a user input in,
    checking if the input value is valid area to move to,
    then updates the player co ordinates to represent the movement.
    The function then calls update_room to update the current_room instance
    """
    global current_room
    try:
        if direction == "c":
            return "placeholder text"
        elif direction in current_room.directions:
            if direction == "north" or direction == "n":
                user.y += 1
            elif direction == "south" or direction == "s":
                user.y -= 1
            elif direction == "east" or direction == "e":
                user.x += 1
            elif direction == "west" or direction == "w":
                user.x += -1
        # This else is in case the user puts in a value that isn't possible to be moved to
            update_room()
        else:
            print("You cannot move there!\n")
            direction_input  = str(input("Please enter a direction to move from this list:" + str(current_room.directions)))
            usage = direction_input[0]
            move(usage)
    except ValueError:
            print("That value isn't recognised!\n")


def update_room():
    """
    The update_room function is called after the player has moved in the move function
    update_room goes through all possible 9 co ordinate locations to check if the co ords are the same as the player position
    if room co ords and player co ords are the same, the current_room variable instance is updated to reflect the new room the player is in
    """
    global current_room

    if user.x == 1:
        if user.y == 1:
            current_room = rooms.room7()
        elif user.y == 2:
            current_room=rooms.room4()
        elif user.y==3:
            current_room=rooms.room1()

    elif user.x == 2:
        if user.y == 1:
            current_room=rooms.room8()
        if user.y==2:
            current_room=rooms.room5()
        if user.y==3:
            current_room=rooms.room2()

    elif user.x == 3:
        if user.y == 1:
            current_room = rooms.room9()
        elif user.y == 2:
            current_room = rooms.room6()
        elif user.y == 3:
            current_room = rooms.room3()

    print("You have moved to " + current_room.room_name() + "\n")


def use_item(input_item):
    global user
    try:
        if input_item == "c":
            return None
        elif input_item in user.inventory:
            if input_item == "map":
                print(user.map())
        else:
            print("You do not have that item!")
            item_input = str(input("Please enter an item to use:")).lower()
            input_item = item_input.split(" ")
            use_item(input_item[0])
    except ValueError:
        print("That isn't a proper value")


def pickup_item(input_item):
    """
    Pickup item works by looking at a file with all the items in each room
    It then finds out which line is the room the player is currently in
    When the user picks up the item it then rewrites the line to remove the picked up item
    and writes the line back to the file
    """
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
    """
    drop_item works by seeing if the item is in the player inventory
    If that is true, then it reads a file with all items in rooms
    it then adds the dropped item to the line that represents the current room
    and removes the item from the user inventory
    """
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
def puzzle():
    global current_room
    current_room.puzzle()


def inventory():
    global user
    print(user.inventory)


def room_items():
    global current_room
    print(current_room.items)


def help():
    """Help function that prints out all available commands"""
    file = open("help.txt", "r")
    print(file.read())
    file.close()


while choice != "q":
    """
    This while loop is the game running
    It takes a user input in to then work out what the corresponding function is to execute the task the user input
    """
    try:
        choice = str(input("Please input what action you would like to do:")).lower()
        choice = choice.split(" ")
        command = choice[0]
        # This try except exists to prevent IndexError incase choice.split does not have 2 values
        try:
            usage = choice[1]
        except IndexError:
            usage = None

        if command == "move" or command == "m":
            move(usage)
        elif command == "inv" or command == "i" or command == "inventory":
            inventory()
        elif command == "items":
            room_items()
        elif command == "puzzle":
            puzzle()
        elif command == "drop" or command == "d":
            drop_item(usage)
        elif command == "pickup" or command == "p" or command == "pickup item":
            pickup_item(usage)
        elif command == "use" or command == "u":
            use_item(usage)
        elif command == "--help":
            help()
        elif command == "q":
            print("Bye Bye World")
            choice = "q"
        else:
            print("That isn't a valid command, enter --help to see available commands\n")
    except ValueError:
        print("That isn't a valid command, enter --help to see available commands\n")
