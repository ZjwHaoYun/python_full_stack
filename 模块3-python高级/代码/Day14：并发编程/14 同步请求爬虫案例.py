import os.path
import time
import requests
import re


def get_page_img_urls(page):
    # 获取页面内容
    res = requests.get(f"https://pic.netbian.com/4kmeinv/index_{page}.html")

    # 使用正则表达式提取图片URL
    ret = re.findall('<img src="(/uploads/allimg/.*?)"', res.text)

    print(ret)
    return ret

def download_page_imgs(img_urls):
    domain = "https://pic.netbian.com/"

    for path in img_urls:
        title = os.path.basename(path)
        url = domain + path
        download_one_img(url, title)


def download_one_img(url, title):
    # 爬虫下载单张图片
    res = requests.get(url)
    # 文件写操作
    with open(f"./imgs/{title}", "wb") as f:
        f.write(res.content)

    print(f"{title}下载成功")


def main():
    start = time.time()
    # for i in range(2, 11):
    page_img_urls = get_page_img_urls(2)

    # 获取页面中的图片URL列表
    download_page_imgs(page_img_urls)
    # 下载页面中的所有图片
    end = time.time()
    print("cost timer:", end - start)


main()
