# TOP ROW OF ROOMS
class room1(object):
    #Variables for the room, this will include the directions that can be traveled
    def __init__(self):
        self.inventory = []

        self.directions = ["east", "e", "south", "s"]

        self.x = 1
        self.y = 3
        self.room_name = 1

        self.solution = "placeholder"
        self.item = "placeholder"

    def look(self):
        return ""


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


    def correct_item(self, user_item):
        if self.item in user_item:
            return True
        else:
            return False


class room2(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["east", "e", "south", "s", "west", "w"]

        self.x = 2
        self.y = 3
        self.room_name = 2

        self.item = "placeholder"
        self.solution = "placeholder"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room3(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["west", "w", "south", "s"]

        self.x = 3
        self.y = 3
        self.room_name = 3

        self.solution = "placeholder"
        self.item = "placeholder"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


# MIDDLE ROW OF ROOMS
class room4(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["east", "e", "north", "n", "south", "s"]

        self.x = 1
        self.y = 2
        self.room_name = 4

        self.solution = "splinter"
        self.item = "keyboard"

    def look(self):
        return "Sitting on a table in this room is a laptop with a message on the screen."

    def room_puzzle(self):
        print("You look at the message on the laptop screen")
        print('{:^50}'.format("I went to the woods and I got IT"))
        print('{:^50}'.format("I couldn't get IT"))
        print('{:^50}'.format("So I left IT there"))
        print('{:^50}'.format("and took IT home with me."))
        return '{:^50}'.format("What was IT?\n")



    def use_item(self, user_item):
            user_solution = input("Please input what you think IT is: ")
            return user_solution


class room5(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["east", "e", "north", "n", "south", "s", "west", "w"]

        self.x = 2
        self.y = 2
        self.room_name = 5

        self.solution = "placeholder"
        self.item = "placeholder"

    def look(self):
        return "In this room is a table with a map on it. The rest of the room is barren"


class room6(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["west", "w", "north", "n", "south", "s"]

        self.x = 3
        self.y = 2
        self.room_name = 6

        self.solution = "placeholder"
        self.item = "placeholder"


    def puzzle(self):
        return "This room is filled to the brim with barrels"

    def look(self):
        return "This room is filled to the brim with barrels"



# BOTTOM ROW OF ROOMS
class room7(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["east", "e", "north", "n"]

        self.x = 1
        self.y = 1
        self.room_name = 7

        self.solution = "placeholder"
        self.item = "placeholder"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room8(room1):
    def __init__(self):
        self.inventory = []
        self.directions = ["east", "e", "north", "n", "west", "w"]
        self.x = 2
        self.y = 1
        self.room_name = 8

        self.solution = "placeholder"
        self.item = "placeholder"

    def look(self):
        return "You look around the room and this function message will change depening on the room"


class room9(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["west", "w", "north", "n"]

        self.x = 3
        self.y = 1
        self.room_name = 9

        self.solution = "placeholder"
        self.item = "placeholder"

    def look(self):
        return "You look around the room and this function message will change depening on the room"
