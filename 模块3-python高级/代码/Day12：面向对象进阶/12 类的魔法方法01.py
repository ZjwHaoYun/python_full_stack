# (1) __new__()方法
"""
1. 开辟独立空间
2. __init__执行
3. 返回该空间地址


"""


# class Person(object):
#
#     def __new__(cls, *args, **kwargs):
#         print("__new__执行")
#         return object.__new__(cls)
#
#     def __init__(self, name, age):
#         print("__init__方法执行")
#         self.name = name
#         self.age = age
#
#
# yuan = Person("yuan", 23)
# print(yuan)
# print(yuan.name)
# print(yuan.age)


# __new__()方法应用

# 版本1
# class Config(object):
#
#     def __init__(self):
#         print("__init__执行了")
#
#
# c1 = Config()
# c2 = Config()
#
# print(id(c1))
# print(id(c2))


# 版本2:单例模式
# class Config(object):
#     instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.instance:
#             cls.instance = object.__new__(cls)
#
#         return cls.instance
#
#     def __init__(self):
#         print("__init__执行了")
#
#
# c1 = Config()
# c2 = Config()
# c3 = Config()
#
# print(id(c1))
# print(id(c2))
# print(id(c3))


