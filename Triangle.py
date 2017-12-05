class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides


# Triangle 클래스를 만든다.
class Triangle(Shape):

    def __init__(self, side1, side2, side3):    # 상속받은 맴버변수까지 Triangle은 4개의 맴버변수를 가진다.
        Shape.number_of_sides = 3
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


t = Triangle(3, 4, 5)

print(t.number_of_sides)
print(t.side2)

