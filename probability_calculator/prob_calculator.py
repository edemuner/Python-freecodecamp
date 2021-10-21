class Hat:

    colors_and_numbers = {}

    def __init__(self, *args):
        for i in args:
            color, number = i.split('=')
            self.colors_and_numbers[color] = number