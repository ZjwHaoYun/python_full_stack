class Animal(object):
    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleep...")


class Dog(Animal):

    def swimming(self):
        print("swimming...")


# 实例对象.变量  查询顺序 [实例空间，类空间，父类空间]
alex = Dog()
alex.swimming()
alex.sleep()
alex.eat()


class Cat(Animal):

    def climb_tree(self):
        print("climb_tree...")


class Bird(Animal):

    def fly(self):
        print("fly...")
