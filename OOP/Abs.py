class Animal:
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        pass


class Goat(Animal):
    def make_sound(self):
        print("bleat")

goat1 = Goat("billy")
goat1.make_sound()