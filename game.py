import rooms
import player
current_room = rooms.room5()
user = player.Player()
choice = ""

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

def update_room():
    global current_room

    #Looks at the x value of the player then looks at the y value to find the correct room

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

while choice != "q":
    try:
        choice = str(input("What action would you like to do?"))
        #This is just fucking movement
        if choice == "move":
            move()
        elif choice == "pos" or choice == "position":
            print(user.x, user.y)

    except ValueError:
        print("That isn't a valid command, enter help to see available commands")
