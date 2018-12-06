import rooms
import player
room = rooms.room1()
#This file will be used to store all the game logic in and other files will be imported into here
# def choice():
#     try:
#         choices = int(input("""What do you want to do? \n0-Find out which room you are currently in \n1-Travel somewhere else \n2-Look around the room \n3-Interact with the room \n4-quit"""))
#     except ValueError:
#         print("Please enter an interger Value")
#     if choices < 0 or choices > 5:
#         print("We don't accept that value")
#         choice()
#     elif choices == 0:
#         print(room.location())
#     elif choices == 1:
#         try:
#             direction_input = str(input("Please enter what direction you would like to travel"))
#         except ValueError:
#             print("Please enter a string value")
#
#         if room.location(direction_input) == True:
#             print("You can travel " + direction_input)
#         else:
#             print("You cannot travel " + direction_input)
#
#     elif choices == 2:
#         print(room.look())
#
#     elif choice == 4:
#         quit()
#
#     choice()
#
# choice()

import six
user = player.Player()
choice = ""
while choice != "q":
    try:
        choice = str(input("What action would you like to do?"))
        if choice == "move":
            try:
                direction = str(input("Please enter a direction to move"))
                direction = direction.lower()
                if direction in room.directions:
                    if direction == "north" or direction == "n":
                        user.y += 1
                    elif direction == "south" or direction == "s":
                        user.y -= 1
                    elif direction == "east" or direction == "e":
                        user.x += 1
                    elif direction == "west" or direction == "w":
                        user.x += -1
                else:
                    print("That value isn't recognised sorry")
            except ValueError:
                print("That value isn't recognised sorry")

        elif choice == "pos" or "position":
            print(user.x, user.y)

    except ValueError:
        print("That isn't a valid command, enter help to see available commands")
