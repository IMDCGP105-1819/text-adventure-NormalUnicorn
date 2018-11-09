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


room = room1()

def choice():
    try:
        choices = int(input("""What do you want to do? \n0-Find out which room you are currently in \n1-Travel somewhere else \n2-Look around the room \n3-Interact with the room \n4-quit"""))
    except ValueError:
        print("Please enter an interger Value")
    if choices < 0 or choices > 5:
        raise Exception("That value isn't an option!")

    if choices == 0:
        print(room.location())
    elif choices == 1:
        try:
            direction_input = str(input("Please enter what direction you would like to travel"))
        except ValueError:
            print("Please enter a string value")

        if room.location(direction_input) == True:
            print("You can travel " + direction_input)
        else:
            print("You cannot travel " + direction_input)

    elif choices == 2:
        print(room.look())

    choice()

choice()
