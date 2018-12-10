class Player(object):
    def __init__(self):
        self.x = 2
        self.y = 2
        self.inventory = {"map":"y", "barrel":"n"}

    def current_inventory(self, inventory, item):
        if item in self.inventory:
            if self.inventory[item] == "n":
                self.inventory[item] == "y"
                print("you now have access to " + item)

x = Player()
x.current_inventory(x.inventory,"barrel")
