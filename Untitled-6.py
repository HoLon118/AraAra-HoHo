class Cat():
    def __init__(self, weight):
        self.weight = weight
    def meow(self):
        print("meow" + "~" * round(self.weight))

年糕 = Cat(7.5)
年糕.meow()