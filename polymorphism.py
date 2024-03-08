

def Driver(car):
    car.drive()

class creta:
    def drive(self):
        print("Driving creta")

class Benz:
    def drive(self):
        print("Driving Benz")

B= Benz()
C= creta()

Driver(B), Driver(C)