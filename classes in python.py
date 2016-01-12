# Example of classes in python including inheritance

class Animal:
    name = ""
    height = 0
    weight = 0
    sound = 0

    def __init__(self, n, h, w, s):
        self.name = n
        self.height = h
        self.weight = w
        self.sound = s

    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name

    def get_type(self):
        print("animal")

    def toString(self):
        return "{} is {} cm tall and of {} kg and makes {} sound".format(self.name, self.height, self.weight, self.sound)


class Dog(Animal):
    owner = ""

    def __init__(self, n, h, w, s, o):
        self.owner = o
        super(Dog, self).__init__(n, h, w, s)

    def set_owner(self, o):
        self.owner = o

    def get_owner(self):
        return self.owner

    def get_sound(self):
        return self.sound

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and of {} kg and makes {} sound and whose owner is {}".format(self.name, self.height, self.weight, self.sound, self.owner)

    #method overloading

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog('bella', 20, 7, 'bhau', 'Meghraj')
print(spot.toString())
