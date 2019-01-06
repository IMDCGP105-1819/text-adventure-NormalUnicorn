class Player(object):
    def __init__(self):
        self.x = 2
        self.y = 2
        self.inventory = []
        self.solved_dict = {"1":"y", "2":"y", "3":"y", "4":"y", "5":"y", "6":"n", "7":"y", "8":"y", "9":"y"}


    def map(self):
        #This function returns the user x y position
        return(self.x, self.y)

    def notebook(self):
        return {k for k, v in self.solved_dict.items() if v == "y"}
