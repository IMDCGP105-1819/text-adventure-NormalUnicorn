# TOP ROW OF ROOMS
class room1(object):
    #Variables for the room, this will include the directions that can be traveled
    def __init__(self):
        self.items = ["barrel"]
        self.directions = ["east", "e", "south", "s"]
        self.x = 1
        self.y = 3

    def room_name(self):
        return "room 1"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


    def puzzle(self):
        print("In the room you see a laptop on a table. On the laptop screen is a riddle: \nI went to the woods and I got it \nI couldn't get it \nSo I left it there \nAnd took it home with me. \n What is it?")
        try:
            ans = str(input("Please enter an answer")).lower()
            if ans == "splinter" or ans == "a splinter":
                print("Congratulations you have now solved this room!")
            elif ans == "c":
                return None
            else:
                print("That is an incorrect answer!")
        except ValueError:
            print("Please put in a correct value")

class room2():
    def __init__(self):
        self.items = []
        self.directions = ["east", "e", "south", "s", "west", "w"]
        self.x = 2
        self.y = 3

    def room_name(self):
        return "room 2"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room3():
    def __init__(self):
        self.items = []
        self.directions = ["west", "w", "south", "s"]
        self.x = 3
        self.y = 3

    def room_name(self):
        return "room 3"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


# MIDDLE ROW OF ROOMS
class room4():
    def __init__(self):
        self.items = []
        self.directions = ["east", "e", "north", "n", "south", "s"]
        self.x = 1
        self.y = 2

    def room_name(self):
        return "room 4"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room5():
    def __init__(self):
        self.items = ["barrel"]
        self.directions = ["east", "e", "north", "n", "south", "s", "west", "w"]
        self.x = 2
        self.y = 2

    def room_name(self):
        return "room 5"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room6():
    def __init__(self):
        self.items = []
        self.directions = ["west", "w", "north", "n", "south", "s"]
        self.x = 3
        self.y = 2

    def room_name(self):
        return "room 6"

    def look(self):
        return "You look around the room and this function message will change depening on the room"



# BOTTOM ROW OF ROOMS
class room7():
    def __init__(self):
        self.items = []
        self.directions = ["east", "e", "north", "n"]
        self.x = 1
        self.y = 1

    def room_name(self):
        return "room 7"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room8():
    def __init__(self):
        self.items = []
        self.directions = ["east", "e", "north", "n", "west", "w"]
        self.x = 2
        self.y = 1

    def room_name(self):
        return "room 8"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room9():
    def __init__(self):
        self.items = []
        self.directions = ["west", "w", "north", "n"]
        self.x = 3
        self.y = 1

    def room_name(self):
        return "room 9"

    def look(self):
        return "You look around the room and this function message will change depening on the room"
