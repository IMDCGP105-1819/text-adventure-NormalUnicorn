import rooms
import player

# Create an instance of the room class that the player is in
current_room = rooms.room5()

user = player.Player()

choice = ""


"""
The function move works by taking a user input in,
checking if the input value is valid area to move to,
then updates the player co ordinates to represent the movement.
The function then calls update_room to update the current_room instance
"""
def move(direction):
    # Takes in user to update their position, and room to check where you can move to
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
        else:
            print("You cannot move there!\n")
            direction_input  = str(input("Please enter a direction to move from this list:" + str(current_room.directions)))
            usage = direction_input[0]
            move(usage)
    except ValueError:
            print("That value isn't recognised sorry\n")

    update_room()

"""
The update_room function is called after the player has moved in the move function
update_room goes through all possible 9 co ordinate locations to check if the co ords are the same as the player position
if room co ords and player co ords are the same, the current_room variable instance is updated to reflect the new room the player is in
"""
def update_room():
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


def item():
    global user
    try:
        input_item = input("Please enter what item you would like to use:")
        if input_item == "map":
            print(user.map())
    except ValueError:
        print("That isn't a proper value")


def puzzle():
    global current_room
    current_room.puzzle()


def pickup():
    global current_room
    global user
    input_item = str(input("please enter an item to pick up:")).lower()
    if input_item == "c":
        return None
    elif input_item in current_room.items:
        if input_item in user.inventory_tracker:
            if user.inventory_tracker[input_item] == "n":
                user.inventory_tracker[input_item] == "y"
                user.inventory.append(input_item)
                print("You picked up " + input_item)
            else:
                print("You already have " + input_item)
    else:
        print("You cannot pick up that item!")


def drop():
    global current_room
    global user
    try:
        input_item = str(input("Please enter an item to drop:")).lower()
        if input_item == "c":
            return None
        elif input_item in user.inventory:
            if user.inventory_tracker[input_item] == "y":
                user.inventory_tracker[input_item] == "n"
                current_room.items.append(input_item)
                user.inventory.remove(input_item)
                print("You have dropped " + input_item)
        else:
            print("You do not have that item to drop!")
    except ValueError:
        print("That is not a recognised value!")

def inventory():
    global user
    print(user.inventory)

def room_items():
    global current_room
    print(current_room.items)

"""Help function that prints out all available commands"""
#TODO try and make this command be responsive as some commands canno always be executed
def help():
    file = open("help.txt", "r")
    print(file.read())
    file.close()


"""
This while loop is the game running
It takes a user input in to then work out what the corresponding function is to execute the task the user input
"""
while choice != "q":
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
        elif command == "room items" or command == "r i":
            room_items(usage)
        elif command == "puzzle":
            puzzle()
        elif command == "drop" or command == "d":
            drop(usage)
        elif command == "pickup" or command == "p" or command == "pickup item":
            pickup(usage)
        elif command == "--help":
            help()
        elif command == "q":
            print("Bye Bye World")
            choice = "q"
        else:
            print("That isn't a valid command, enter --help to see available commands\n")
    except ValueError:
        print("That isn't a valid command, enter --help to see available commands\n")

#TODO make statements check if input in command
