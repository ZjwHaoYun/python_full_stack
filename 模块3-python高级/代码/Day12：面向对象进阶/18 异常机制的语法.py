from loguru import logger

# (1) 语法结构1:
# try:
#     # print(yuan)
#     [1,2,3][3]
#     {"a":"apple"}["banana"]
#
# except NameError as e:
#     print("e:::", e)

# (2) 语法结构2:

# try:
#     {"a": "apple"}["banana"]
#     [1, 2, 3][3]
#     print(yuan)
#
#
# except NameError as e:
#     print("e:::", e)
#
# except IndexError as e:
#     print("e:::", e)
#
# except KeyError as e:
#     print("e:::", e, dir(e), type(e))


# (3) 语法结构3:

# try:
#
#     {"a": "apple"}["b"]
#     print(yuan)
#     [1, 2, 3][3]
#
# except (NameError, IndexError, KeyError) as e:
#     logger.error(f"{e}")

# (4) 通用错误类型
# try:
#     123
#     yuan
#
# except Exception as e:
#     print(e)


#  (5)

"""
try:
    pass  # 正常执行语句
except Exception as e:
    pass  # 异常处理语句
else:
    pass # 测试代码没有发生异常 
finally:
    pass  # 无论是否发生异常一定要执行的语句,比如关闭文件，数据库或者socket
    

"""
f = None
try:

    f = open("apple.txt", mode="w")
    # yuan

except NameError as e:
    print("e:::", e)

finally:
    # 资源回收的
    print("资源回收")
    f.close()
