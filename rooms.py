class room1:
    def __init__(self):
        self.directions = ["North", "South", "East", "West"]

    def travel(self, inputs):
        if inputs in self.directions:
            return True
        else:
            return False

    def location(self):
        return "You are currently in room 1"

    def look(self):
        return "You look around the room and this function message will change depening on the room"
