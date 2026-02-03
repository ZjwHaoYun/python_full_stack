class Animal(object):
    def eat(self):
        print("eating...")

    def sleep(self):
        print("self:::", id(self))
        print("sleep...")


class Dog(Animal):

    def swimming(self):
        print("swimming...")


alex = Dog()


class Fly(object):
    def fly(self):
        print("flying")


class Eagle(Animal, Fly):
    pass


class Bat(Animal, Fly):
    pass


b1 = Bat()
b1.fly()

e1 = Eagle()
e1.fly()
