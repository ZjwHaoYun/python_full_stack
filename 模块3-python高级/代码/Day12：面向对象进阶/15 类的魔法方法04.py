# class Cache(object):
#
#     def __init__(self):
#         self.data = {}
#
#     def add(self, key, val):
#         # if 环境判断 或数据判断
#         self.data[key] = val
#
#     def remove(self, key):
#         self.data.pop(key)
#
#     def show(self):
#         print(self.data)
#
#     def __len__(self):
#         return len(self.data)


# 版本1
# cache = Cache()
# cache.add("name", "yuan")
# cache.add("age", 18)
# cache.show()
# cache.remove("age")
# cache.show()
#
# print(len(cache))

# 版本2

from loguru import logger


class Cache(object):

    def __init__(self):
        self.__data = {}

    # def __getitem__(self, item):
    # if 环境判断 或数据判断
    # self.data[key] = val

    def __setitem__(self, key, value):
        # 有效控制，判断，监控，日志
        self.__data[key] = value
        logger.info(f"已经向self.__data添加了{key}和{value}")

    def __getitem__(self, key):
        # 有效控制，判断，监控，日志
        # return self.__data.get(key)
        val = self.__data.get(key)
        if val:
            return val
        else:
            raise KeyError(f"{key}键不存在")

    def __delitem__(self, key):
        # 有效控制，判断，监控，日志
        del self.__data[key]

    def __contains__(self, key):
        # 有效控制，判断，监控，日志
        return key in self.__data


cache = Cache()
# cache["name"] = "yuan"
# print(cache["name"])
# del cache["name"]
# print(cache["name"])
print("name" in cache)
