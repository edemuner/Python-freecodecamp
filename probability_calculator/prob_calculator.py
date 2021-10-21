class Hat:

    contents = []

    def __init__(self, *args):
        for i in args:
            color, number = i.split('=')
            for j in range(int(number)):
                self.contents.append(color)