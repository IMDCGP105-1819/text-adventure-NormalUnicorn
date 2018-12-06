class room1(object):
    #Variables for the room, this will include the directions that can be traveled
    def __init__(self):
        self.directions = ["north", "south", "east", "west", "n", "s", "e", "w"]
        self.x = 1
        self.y = 3

    def travel(self, inputs):
        if inputs in self.directions:
            return True
        else:
            return False

    def location(self):
        return "You are currently in room 1"

    def look(self):
        return "You look around the room and this function message will change depening on the room"

class room2():
    def __init__(self):
        self.directions = []
        self.x = 2
        self.y = 3

class room3():
    def __init__(self):
        self.directions = []
        self.x = 3
        self.y = 3

class room4():
    def __init__(self):
        self.directions = []
        self.x = 1
        self.y = 2


class room5():
    def __init__(self):
        self.directions = []
        self.x = 2
        self.y = 2

class room6():
    def __init__(self):
        self.directions = []
        self.x = 3
        self.y = 2

class room7():
    def __init__(self):
        self.directions = []
        self.x = 1
        self.y = 1

class room8():
    def __init__(self):
        self.directions = []
        self.x = 2
        self.y = 1

class room9():
    def __init__(self):
        self.x = 3
        self.directions = []
        self.y = 1
