# TOP ROW OF ROOMS
class room1(object):
    #Variables for the room, this will include the directions that can be traveled
    def __init__(self):
        self.inventory = []

        self.directions = ["east", "e", "south", "s"]

        self.look = "placeholder text"

        self.x = 1
        self.y = 3
        self.room_name = 1

        self.solution = "umbrella"
        self.item = "keyboard"

    def room_puzzle(self):
        print("You look at the message on the screen")
        return '{:^50}'.format("What can go up a chimely down, but not down a chimely up?\n")



    def use_item(self, user_item):
            user_solution = input("Please input what you think the answer is:")
            return user_solution

    def correct_item(self, user_item):
        if self.item in user_item:
            return True
        else:
            return False




class room2(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["east", "e", "south", "s", "west", "w"]

        self.look = "placeholder text"

        self.x = 2
        self.y = 3
        self.room_name = 2

        self.solution = "dentist"

    def room_puzzle(self):
        print("You look at the message on the screen")
        print("I dig out tiny caves, and store gold and silver in them. I also build bridges of silver and make crowns of gold. Sooner or later everybody needs my help")
        return '{:^50}'.format("Who am I?\n")


class room3(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["west", "w", "south", "s"]

        self.look = "more placeholder text"

        self.x = 3
        self.y = 3
        self.room_name = 3

        self.solution = "night"


    def room_puzzle(self):
        return '{:^50}'.format("What falls, but does not break, while its opposite breaks but does not fall\n")


# MIDDLE ROW OF ROOMS
class room4(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["east", "e", "north", "n", "south", "s"]

        self.look = "more and more placeholder text"

        self.x = 1
        self.y = 2
        self.room_name = 4

        self.solution = "splinter"
        self.item = "keyboard"

    def room_puzzle(self):
        print("You look at the message on the screen")
        print('{:^50}'.format("I went to the woods and I got IT"))
        print('{:^50}'.format("I couldn't get IT"))
        print('{:^50}'.format("So I left IT there"))
        print('{:^50}'.format("and took IT home with me."))
        return '{:^50}'.format("What was IT?\n")


class room5(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["east", "e", "north", "n", "south", "s", "west", "w"]

        self.look = "more and more placeholder text"

        self.x = 2
        self.y = 2
        self.room_name = 5

        self.solution = "placeholder"
        self.item = "placeholder"

    def room_puzzle(self):
        return "There is no puzzle in this room."



class room6(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["west", "w", "north", "n", "south", "s"]

        self.look = "more and more placeholder text"

        self.x = 3
        self.y = 2
        self.room_name = 6

        self.solution = "barrel"
        self.item = "barrel"

    def puzzle(self):
        return "This room is filled to the brim with barrels"


# BOTTOM ROW OF ROOMS
class room7(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["east", "e", "north", "n"]

        self.look = "more and more and more placeholder text"

        self.x = 1
        self.y = 1
        self.room_name = 7

        self.solution = "tongue"

    def room_puzzle(self):
        print("You look at the message on the screen")
        return '{:^50}'.format("What tastes better than it smells?\n")


class room8(room1):
    def __init__(self):
        self.inventory = []
        self.directions = ["east", "e", "north", "n", "west", "w"]
        self.x = 2
        self.y = 1
        self.room_name = 8

        self.look = "more and more and more placeholder text"
        self.solution = "leaves"

    def room_puzzle(self):
        print("You look at the message on the screen")
        print("Walk on the living, they don't even mumble.\nWalk on the dead, they mutter and grumble.")
        return '{:^50}'.format(" What are they\n")


class room9(room1):
    def __init__(self):
        self.inventory = []

        self.directions = ["west", "w", "north", "n"]

        self.look = "final placeholder text"

        self.x = 3
        self.y = 1
        self.room_name = 9

        self.solution = "short"
        
    def room_puzzle(self):
        print("You look at the message on the screen")
        return '{:^50}'.format("What gets shorter when you add two letters to it?\n")
