class Iphone6:
    def home(self):
        print("this is Iphone6 Button")

class IphoneX(Iphone6):
    def home(self):
        print("this is IphoneX Touch")
        super().home()

I6 = Iphone6()
I6.home()

I10 = IphoneX()
I10.home()