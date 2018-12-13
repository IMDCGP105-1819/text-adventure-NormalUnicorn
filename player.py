class Player(object):
    def __init__(self):
        self.x = 2
        self.y = 2
        self.inventory_tracker = {"map":"y", "barrel":"n"}
        self.inventory = ["map"]



    """
    this function works by taking in the item the user wants to use and their current inventory
    it checks if they have access to the item or not
    currently it allows the user access if they don't have access for testing purposes
    """
    #TODO if the user inputs an item that isn't in their inventory let them know
    #This whole function is a TODO
    
    """
    This function returns the user x y position
    """



    def map(self):
        return(self.x, self.y)
