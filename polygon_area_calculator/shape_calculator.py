class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self. height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5


    def get_picture(self):
        pic = ''
        for i in range(self.height):
            pic += self.width * '*' + '\n'
        return pic

    def get_amount_inside(self, other_rectangle):
        return self.get_area() // other_rectangle.get_area()


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(Side={self.width})'


