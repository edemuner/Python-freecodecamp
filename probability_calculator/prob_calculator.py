import random

class Hat:

    contents = []

    def __init__(self, **kwargs):
        for i, j in kwargs.items():
            for l in range(j):
                self.contents.append(i)


    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        else:
            return random.sample(self.contents, number)


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