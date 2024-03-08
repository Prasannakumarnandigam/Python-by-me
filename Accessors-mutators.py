class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def getlength(self):
        return self.length

    def getbreadth(self):
        return self.breadth

    def setlength(self, l):
        self.length = l

    def setbreadth(self, b):
        self.breadth = b

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * self.length + 2 * self.breadth

r = Rectangle(10,5)
print(r.getlength())
print(r.getbreadth())
r.setlength(20)
r.setbreadth(40)

print(r.area())

