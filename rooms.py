# TOP ROW OF ROOMS
class room1(object):
    #Variables for the room, this will include the directions that can be traveled
    def __init__(self):
        self.directions = ["east", "e", "south", "s"]
        self.x = 1
        self.y = 3

    def room_name(self):
        return "room 1"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room2():
    def __init__(self):
        self.directions = ["east", "e", "south", "s", "west", "w"]
        self.x = 2
        self.y = 3

    def room_name(self):
        return "room 2"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room3():
    def __init__(self):
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
        self.directions = ["east", "e", "north", "n", "south", "s"]
        self.x = 1
        self.y = 2

    def room_name(self):
        return "room 4"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room5():
    def __init__(self):
        self.directions = ["east", "e", "north", "n", "south", "s", "west", "w"]
        self.x = 2
        self.y = 2

    def room_name(self):
        return "room 5"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room6():
    def __init__(self):
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
        self.directions = ["east", "e", "north", "n"]
        self.x = 1
        self.y = 1

    def room_name(self):
        return "room 7"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room8():
    def __init__(self):
        self.directions = ["east", "e", "north", "n", "west", "w"]
        self.x = 2
        self.y = 1

    def room_name(self):
        return "room 8"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room9():
    def __init__(self):
        self.directions = ["west", "w", "north", "n"]
        self.x = 3
        self.y = 1

    def room_name(self):
        return "room 9"

    def look(self):
        return "You look around the room and this function message will change depening on the room"
