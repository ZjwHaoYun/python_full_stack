class Student(object):

    def __init__(self, name, score):
        self.__name = name
        # 私有化：__score
        # 外部代码不能随意修改对象内部的状态
        self.__score = score

    # 开放的一个查询成绩的接口
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if isinstance(score, int) and 0 < score < 100:
            self.__score = score
        else:
            raise ValueError("数据错误")



yuan = Student("yuan", 88)

# 案例1
# print(yuan.name)
# print(yuan.score)
# yuan.score = 100
# print(yuan.score)

# 案例2

# print(yuan.name)
# print(yuan.__score)
# print(yuan.get_score())
# yuan.__score = 1000
# yuan.set_score(99)
# print(yuan.get_score())


# 案例3

# class Student2(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         # 私有化：__score
#         self.score = score
#
#
# rain = Student2("rain", 88)
#
# rain.score = "hello world"
# yuan.set_score("hello yuan")
