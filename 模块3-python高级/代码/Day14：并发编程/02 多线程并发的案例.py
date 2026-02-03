import threading
import time

import requests
import re


# (1) 爬虫与文件操作回顾
# 下载一张图片
# res = requests.get(" https://pic.netbian.com/uploads/allimg/240301/195902-17092943422161.jpg")
#
# with open("a.jpg", mode="wb") as f:
#     f.write(res.content)

# (2) 批量下载图片

# start = time.time()
# # 爬取10页img
# n = 1
# for page in range(2, 12):
#     # 爬取一页img
#     res = requests.get(f"https://pic.netbian.com/index_{page}.html")
#     # print(res.text)
#
#     ret = re.findall("/uploads/allimg/.*?.jpg", res.text)
#     print(ret)
#
#     domain = "https://pic.netbian.com"
#     for path in ret:
#         url = domain + path
#         res = requests.get(url)
#         with open(f"./imgs/{n}.jpg", mode="wb") as f:
#             f.write(res.content)
#
#         print(f"{n}.jpg下载成功！")
#         n += 1
#
# print("耗时:", time.time() - start)


# (3) 多线程并发

def get_one_img(path, n):
    domain = "https://pic.netbian.com"
    url = domain + path
    res = requests.get(url)
    with open(f"./imgs/{n}.jpg", mode="wb") as f:
        f.write(res.content)

    # print(f"{n}.jpg下载成功！")


def main():
    start = time.time()
    # 爬取10页img
    n = 1
    t_list = []
    for page in range(2, 10):
        # 爬取一页img
        res = requests.get(f"https://pic.netbian.com/index_{page}.html")
        # print(res.text)

        ret = re.findall("/uploads/allimg/.*?.jpg", res.text)
        # print(ret)

        for path in ret:
            # get_one_img(path,n)
            # 创建线程对象
            t = threading.Thread(target=get_one_img, args=(path, n))
            t.start()
            t_list.append(t)

            n += 1

    for t in t_list:
        t.join()
    print("耗时:", time.time() - start)


if __name__ == '__main__':
    main()
