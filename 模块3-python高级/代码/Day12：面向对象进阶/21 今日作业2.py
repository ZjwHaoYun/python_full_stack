# (6)
# class BankAccount(object):
#     def __init__(self, account_num, balance=0):
#         self.__account = account_num
#         self.__balance = balance
#
#     def deposit(self, mount):
#         print(f"{self.__account}存款{mount}元！")
#         self.__balance += mount
#
#     def withdraw(self, mount):
#
#         if self.__balance >= mount:
#             self.__balance -= mount
#             print(f"{self.__account}取款{mount}元，当前余额：{self.__balance}")
#         else:
#             print("提取金额大于余额！")
#
#     def get_balance(self):
#
#         # if判断
#         return self.__balance
#
#     def __deduct_fees(self):
#         print("扣除手续费")
#
#     def process_monthly_fees(self):
#         self.__deduct_fees()
#         print("月度扣费完成！")
#
#
# account01 = BankAccount("123456", 10000)

# print(account01.__dict__)
# print(account01._BankAccount__account)
# print(account01._BankAccount__balance)
# print(account01.get_balance())
# account01.process_monthly_fees()
# account01._deduct_fees()


# (9)
# key必须是字符串操作
# d = {}

# d["name"] = "yuan"
# d["age"] = 18
#
# print(d["name"])
#
# del d["age"]
#
# print(d)

# d[1000] = "apple"
# print(d)


# class MyDict(object):
#
#     def __init__(self):
#         self.data = {}
#
#     def __getitem__(self, item):
#         if isinstance(item, str):
#             return self.data[item]
#         else:
#             raise TypeError("Key must be string！")
#
#     def __setitem__(self, key, value):
#         if isinstance(key, str):
#             self.data[key] = value
#         else:
#             raise TypeError("Key must be string！")
#
#     def __delitem__(self, key):
#         if isinstance(key, str):
#             if key in self.data:
#                 del self.data[key]
#             else:
#                 raise TypeError("Key must be in data!")
#         else:
#             raise TypeError("Key must be string！")
#
#
# d = MyDict()
#
# d["name"] = "yuan"
# print(d.data)
# d[1000] = "apple"

# print(d["name"])
# print(d[1000])

# del d[1000]
# del d["name"]
# print(d.data)


# (10)