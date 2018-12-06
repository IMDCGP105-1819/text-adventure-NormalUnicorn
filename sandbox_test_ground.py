class test(object):
    def __init__(self):
        self.rooms = {1:'y', 2:'n', 3:'n', 4:'y'};

    def draw(self):
        for x in range(0,9):
            value = rooms.value(x+1)
            if value == 'y':
                print("Passed room " + x)
                x+=1
            elif value == 'n':
                x=15

r = test
r.draw(r)
