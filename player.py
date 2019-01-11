class Player(object):
    def __init__(self):
        self.x = 2
        self.y = 2
        self.inventory = []
        self.solved_dict = {"1":"n", "2":"n", "3":"n", "4":"n", "5":"y", "6":"y", "7":"n", "8":"n", "9":"n"}


    def map(self):
        #This function returns the user x y position
        return(self.x, self.y)

    def notebook(self):
        #https://stackoverflow.com/questions/42438808/finding-all-the-keys-with-the-same-value-in-a-python-dictionary
        return {k for k, v in self.solved_dict.items() if v == "y"}
