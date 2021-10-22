import random
import copy

class Hat:

    contents = []

    def __init__(self, *args):
        for i in args:
            color, number = i.split('=')
            for j in range(int(number)):
                self.contents.append(color)

    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        else:
            return random.sample(self.contents, number)


def experiment(hat,
               expected_balls,
               num_balls_drawn,
               num_experiments):
    pass