from math import pi


class Circle:

    def __init__(self, r):
        self.radius = r


    def area(self):
        return pi* self.radius * self.radius

    def perimeter(self):
        return 2*pi*self.radius


c1 = Circle(10)
print(c1.area())
print(c1.perimeter())