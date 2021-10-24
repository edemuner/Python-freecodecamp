import random

class Hat:

    contents = []

    def __init__(self, *args):
        for i in args:
            i = Color(i)
            color, number = i.split('=')
            for j in range(int(number)):
                self.contents.append(color)

    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        else:
            return random.sample(self.contents, number)

class Color:
    def __init__(self, color_name):
        self.color_name = color_name


def experiment(hat,
               expected_balls,
               num_balls_drawn,
               num_experiments):
    times = 0

    for exp in range(num_experiments):

        for ball, number in expected_balls.items():
            if hat.draw(num_balls_drawn).count(ball) == number:
                times += 1

    return times / num_experiments