class Rectangle:

    count = 0  #static variable


#constructor
    def __init__(self, length, breadth):
        self.length= length #instance variable
        self.breath= breadth  #instance variable

#methods
    def perimeter(self):
        return 2*self.length + self.breath

    def area(self):
        return self.length * self.breath

    @staticmethod #decorator
    def isSquare(length , breadth):
        return length == breadth




r1 = Rectangle(10,5)
print(r1.perimeter())

r2 = Rectangle(5, 5)
print(r2.area())

#r5.Rectangle.isSquare(10,5)
print(Rectangle.isSquare(10,10))
