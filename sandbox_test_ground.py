class Player(object):
    def __init__(self):
        self.x = 2
        self.y = 2
        self.inventory = {"map":"y", "barrel":"n"}

    def current_inventory(self, inventory, item):
        item = item.lower()
        if item in self.inventory:
            if self.inventory[item] == "n":
                self.inventory[item] == "y"
                print("you now have access to " + item)
            elif self.inventory[item] == "y":
                print("you already have access to that item!")


    def map(self):
        if self.inventory["map"] == "n":
            print("You currently do not have access to the map sorry!")
            return None
        else:
            print("You have access to the map!")

        print(self.x, self.y)



x = Player()
x.inventory["map"] == "n"
x.current_inventory(x.inventory,"map")
x.map()
