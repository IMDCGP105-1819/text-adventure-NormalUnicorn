class Player(object):
    def __init__(self):
        self.x = 2
        self.y = 2
        self.inventory_tracker = {"map":"y", "barrel":"n"}
        self.inventory = []



    """
    this function works by taking in the item the user wants to use and their current inventory
    it checks if they have access to the item or not
    currently it allows the user access if they don't have access for testing purposes
    """
    #TODO if the user inputs an item that isn't in their inventory let them know
    #This whole function is a TODO
    def current_inventory(self, inventory):
        for item in self.inventory_tracker:
            if self.inventory_tracker[item] == "n":
                return None
            elif self.inventory_tracker[item] == "y":
                self.inventory.append(item)

        print(self.inventory)
    """
    This function returns the user x y position
    """



    def map(self):
        return(self.x, self.y)
