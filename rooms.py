class room1:
    def __init__(self):
        self.directions = ["North", "South", "East", "West"]

    def travel(self, inputs):
        if inputs in self.directions:
            print("You can travel " + inputs)
        else:
            print("You cannot travel" + inputs)

player = room1()
player.travel("west")
