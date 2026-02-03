# print(len(100))
# print(len([1, 2, 3]))
# print(len({"a": "apple"}))
# list
# dict

# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = l2
# print(l1 == l2) # 值判断
# print(l1 is l2) # 是都一样
# print(l2 is l3) # 是都一样

# 缓存的容器类型
class Cache(object):

    def __init__(self):
        self.data = []

    def add(self, item):
        # if 环境判断 或数据判断
        self.data.append(item)

    def remove(self, item):
        self.data.remove(item)

    def show(self):
        print(self.data)

    def __len__(self):

        return  len(self.data)


cache = Cache()
cache.add("yuan")
cache.add("rain")
cache.add("alvin")

cache.show()
cache.remove("yuan")
cache.show()

print(len(cache))


# data = []
# data.append("yuan")
# data.append("rain")
# data.append("alvin")
# data.remove("yuan")
