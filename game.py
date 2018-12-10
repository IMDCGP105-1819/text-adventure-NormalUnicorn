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
def move():
    # Takes in user to update their position, and room to check where you can move to
    global current_room
    try:
        direction = str(input("Please enter a direction to move"))
        direction = direction.lower()
        if direction == "c":
            return None
        elif direction in current_room.directions:
            if direction == "north" or direction == "n":
                user.y += 1
            elif direction == "south" or direction == "s":
                user.y -= 1
            elif direction == "east" or direction == "e":
                user.x += 1
            elif direction == "west" or direction == "w":
                user.x += -1
        else:
            print("You cannot move there!")
            move()
    except ValueError:
            print("That value isn't recognised sorry")
        # This else is in case the user puts in a value that isn't possible to be moved to
    current_room = update_room()


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

    return current_room

"""Help function that prints out all available commands"""
#TODO try and make this command be responsive as some commands canno always be executed
def help():
    print("This is a list of available commands:")


"""
This while loop is the game running
It takes a user input in to then work out what the corresponding function is to execute the task the user input
"""
while choice != "q":
    try:
        choice = str(input("What action would you like to do? \n"))
        #This is just fucking movement
        if choice == "move":
            move()
        elif choice == "pos" or choice == "position":
            print(user.x, user.y, "\n")
        elif choice == "--help":
            help()
        else:
            print("That isn't a valid command, enter --help to see available commands")
    except ValueError:
        print("That isn't a valid command, enter --help to see available commands")
