from shape_calculator import Rectangle

rectangle = Rectangle(5, 5)
rectangle2 = Rectangle(30, 20)


print(rectangle.get_picture())
print(rectangle2.get_picture())

print(rectangle.get_area())
print(rectangle2.get_area())
print(rectangle2.get_amount_inside(rectangle))

print(rectangle)
print(rectangle2)