# 一、type 和isinstance


# class Animal(object):
#     def eat(self):
#         print("eating...")
#
#     def sleep(self):
#         print("self:::", id(self))
#         print("sleep...")
#
#
# class Dog(Animal):
#
#     def swimming(self):
#         print("swimming...")
#
#
# alex = Dog()
#
# print(type(alex))
# print(isinstance(alex, Dog))
# print(isinstance(alex, Animal))


# 二、dir函数和__dict__

class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def test(self):
        pass


alex = Student("alex", 32)

# print(alex.__dict__)

print(dir(alex))
print(alex.__class__)
