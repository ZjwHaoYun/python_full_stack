# class Animal(object):
#     def eat(self):
#         print("eating...")
#
#     def sleep(self):
#         self.swimming()
#         print("self:::", id(self))
#         print("sleep...")
#
#
# class Dog(Animal):
#
#     def swimming(self):
#         print("swimming...")

# 实例对象.变量  查询顺序 [实例空间，类空间，父类空间,...]
# alex = Dog()
# print(id(alex))
# alex.sleep()


# class Cat(Animal):
#     pass
#
# c = Cat()
# c.sleep()


# 重写父类方法


class Animal(object):
    def eat(self):
        print("eating...")

    def sleep(self):
        print("self:::", id(self))
        print("sleep...")


class Dog(Animal):

    def swimming(self):
        print("swimming...")

    def sleep(self):
        # print("sleep...")
        # 调用父类原方法
        # 方式1： 类对象.方法(self,其他参数)
        # Animal.sleep(self)
        # 方式2： super
        # super().sleep()
        print("侧翻睡")


# 实例对象.变量  查询顺序 [实例空间，类空间，父类空间,...]
alex = Dog()
print(id(alex))
alex.sleep()
