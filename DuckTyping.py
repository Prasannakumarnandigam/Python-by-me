def petLover(pet):
    if hasattr(pet, 'talk'):
        pet.talk()

    if hasattr(pet, 'walk'):  # to aviod run time error, hasattr -> has Attribute
        pet.walk()



class duck:
    def talk(self):
        print("Duck talking")

    def walk(self):
        print("Duck walking")

class dog:
    def talk(self):
        print("Dog talking")

    def walk(self):
        print("Dog walking")

c = dog()
petLover(c)

d = duck()
petLover(d)