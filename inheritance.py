class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * self.length + self.breadth

class cubiod(Rectangle):
    def __init__(self, l, b, h):
        super().__init__(l, b)
        self.height = h

    def volume(self):
        return self.length * self.breadth * self.height

c1 = cubiod(3, 5 ,10)
print(c1.volume())
