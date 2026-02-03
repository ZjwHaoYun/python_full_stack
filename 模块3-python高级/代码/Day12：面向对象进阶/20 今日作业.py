import math

# (1) 关于继承与方法重写
# class A:
#     def get(self):
#         self.say()
#
#     def say(self):
#         print('apple')
#
#
# class B(A):
#     def say(self):
#         print('banana')
#
#
# b = B()
# b.get()

# (2) 将以下代码填写完整

# class A:
#     def foo(self, x):
#         print('executing class_foo(%s, %s)' % (self, x))
#
#     @classmethod
#     def class_foo(cls, x):
#         print('executing class_foo(%s, %s)' % (cls, x))
#
#     @staticmethod
#     def static_foo(x):
#         print('executing static_foo(%s)' % (x))
#
#
# a = A()
#
# # 调用 foo 函数,参数传入 10
# a.foo(10)
# # 调用 class_foo 函数,参数传入20
# A.class_foo(20)
# # 调用 static_foo 函数,参数传入30
# # 方式1:实例对象调用
# a.static_foo(30)
# # 方式2:类对象
# A.static_foo(30)


# (3)  创建一个名为 `Circle` 的类，具有 `radius` 属性

# class Circle(object):
#
#     def __init__(self, radius):
#         self.radius = radius
#     @property
#     def calculate_area(self):
#         return round(math.pi * self.radius * self.radius, 2)
#
#     @property
#     def calculate_circumference(self):
#         return round(2 * math.pi * self.radius, 2)
#
#     @property
#     def calculate_diameter(self):
#         return 2 * self.radius
#
#
# c1 = Circle(10)
# print(c1.calculate_area)
# print(c1.calculate_circumference)


# (4) 创建一个名为 `Product` 的类，具有 `name` 和 `price` 属性。实现 `__str__` 方法，使其返回格式为 "Product: name - price" 的字符串表示。同时实现 `__len__` 方法，使其返回产品名称的长度。


# class Product(object):
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f"Product: {self.name} - {self.price}"
#
#
# p1 = Product("iphone", 19999)
# print(p1)
# # print(id(p1))
# p2 = Product("Mac", 29999)
# print(p2)
# # print(id(p2))


# (5) 实现一个FTP类，`FTP`类包含了`get`和`post`两个方法，分别用于下载和上传文件。`run`方法首先引导用户输入命令（`get`或`post`），然后根据用户输入的命令和文件名，使用反射机制执行对应的类方法。


# class FTP(object):
#
#     def __init__(self):
#         pass
#
#     def run(self):
#         print("start...")
#         # self.post()
#         # self.get()
#         while 1:
#             inp = input("【get 文件｜post 文件】")
#
#             cmd = inp.split(" ")[0]
#
#             # if cmd == "get":
#             #     self.get()
#             # elif cmd == "post":
#             #     self.post()
#
#             # 基于反射机制返程方法的分发
#             if hasattr(self, cmd):
#                 func = getattr(self, cmd)
#                 func()
#
#     def post(self):
#         print("上传文件")
#
#     def get(self):
#         print("下载文件")
#
#
# ftp = FTP()
# ftp.run()
