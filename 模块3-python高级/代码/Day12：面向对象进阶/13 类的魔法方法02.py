# (2) __str__方法
# class Person(object):
#
#     def __init__(self, name, age):
#         print("__init__方法执行")
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         print("__str__执行...")
#         # return 100
#         return f"姓名：{self.name} 年龄：{self.age}"
#
# yuan = Person("yuan", 23)
# # 触发__str__执行的是str()
#
# # print(str(yuan))
# print(yuan)
# alex = Person("alex", 33)
# print(alex)

# (3) __eq__方法

# 案例1
# class Person(object):
#
#     def __init__(self, name, age):
#         print("__init__方法执行")
#         self.name = name
#         self.age = age
#
#     # 触发机制： ==
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age
#
#
# yuan = Person("xxx", 23)
#
# alex = Person("xxx", 23)
# # print(alex == 1)
# print(alex == yuan)

# 案例2
class Dog(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        print("Dog __eq__")
        return self.age == other.age


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 触发机制： ==
    def __eq__(self, other):
        print("Person __eq__")
        return self.name == other.name and self.age == other.age


yuan = Person("yuan", 23)
alex = Dog("alex", 23)

# print(yuan == alex)
print(alex == yuan)

