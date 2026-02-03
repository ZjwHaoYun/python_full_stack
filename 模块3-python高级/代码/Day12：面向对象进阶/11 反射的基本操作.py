class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


yuan = Person("yuan", 22, "male")

# 对象.属性变量
# print(yuan.name)
# yuan.age = 100
# print(yuan.age)

while 1:
    attr = input("请输入您想查询的yuan的某个属性:")

    # print(yuan.attr)
    # 方案1
    # if attr == "name":
    #     print(yuan.name)
    # elif attr == "age":
    #     print(yuan.age)

    # 方案2:反射

    # print(getattr(yuan,"name")) # yuan.name
    # print(getattr(yuan,"age")) # yuan.age

    if hasattr(yuan, attr):
        val = getattr(yuan, attr)
        print(f"yuan的{attr}的属性值：{val}")
    else:
        print(f"yuan没有{attr}属性")
        choice = input("是否给yuan加入该属性【Y/N】")

        if choice.lower() == "y":
            value = input(f"请输入yuan对象{attr}一个确定值：")
            setattr(yuan, attr, value)
