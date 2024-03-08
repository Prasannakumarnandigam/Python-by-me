class Cubiod:
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h

    def lidArea(self):
        return self.length * self.breadth

    def totalArea(self):
        return 2 * self.length * self.breadth

    def volume(self):
        return self.length * self.breadth * self.height


c1 = Cubiod(10, 20, 30)
print(c1.lidArea())

c2 = Cubiod(1, 20 , 100)
print(c2.volume())

c3 = Cubiod(2 , 3 , 4)
print(c3.totalArea())