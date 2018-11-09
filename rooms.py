class room1:
    def __init__(self):
        self.directions = ["North", "South", "East", "West"]

    def travel(self, inputs):
        if inputs in self.directions:
            return "You can travel " + inputs
        else:
            return "You cannot travel "  + inputs

    def location(self):
        return "You are currently in room 1"


room = room1()
direction_input = input("Please enter which direction you want to travel in")
print(room.travel(direction_input))
print(room.location())
