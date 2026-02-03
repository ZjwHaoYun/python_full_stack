import os.path
import time
import re
import asyncio
import aiohttp


async def get_page_img_urls(page):
    # 获取页面内容
    # requests：同步请求模块
    # res = requests.get(f"https://pic.netbian.com/4kmeinv/index_{page}.html")
    # aiohttp:异步请求模块

    # 需要一个异步的上下文环境管理
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://pic.netbian.com/4kmeinv/index_{page}.html",verify_ssl=False) as res:
            data = await res.content.read()
            # 使用正则表达式提取图片URL
            ret = re.findall('<img src="(/uploads/allimg/.*?)"', data.decode("gbk"))

            print(ret)
            return ret


async def download_page_imgs(img_urls):
    domain = "https://pic.netbian.com/"

    for path in img_urls:
        title = os.path.basename(path)
        url = domain + path
        await download_one_img(url, title)


async def download_one_img(url, title):
    # 爬虫下载单张图片
    # res = requests.get(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url,verify_ssl=False) as res:
            data = await res.content.read()
            # 文件写操作
            with open(f"./imgs/{title}", "wb") as f:
                f.write(data)

            print(f"{title}下载成功")


async def main():
    start = time.time()
    # for i in range(2, 11):
    page_img_urls = await get_page_img_urls(2)

    # 获取页面中的图片URL列表
    await download_page_imgs(page_img_urls)
    # 下载页面中的所有图片
    end = time.time()
    print("cost timer:", end - start)


asyncio.run(main())
