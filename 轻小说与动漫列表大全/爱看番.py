# -*- coding:utf-8 -*-
import random
import time
from tqdm import tqdm
import requests
from pyquery import PyQuery as pq

"""
获取SF互动传媒网的轻小说大全
@:param url：http://www.ikanfan.com/dongman/index{页数，从1开始}.html

@:return txt整理文档
"""

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.ikanfan.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}


def get_info():
    start_page = int(input("请输入查询起始页码："))
    pages = int(input("请输入查询页数："))
    for page in tqdm(range(start_page, pages + 1)):
        url = "http://www.ikanfan.com/dongman/index{}.html".format(page)
        try:
            response = requests.get(url=url, headers=headers, timeout=10)
            if response.status_code == 200:
                # pyquery初始化字符
                doc = pq(response.text)
                contents = doc(".clearfix .mt15 #contents a")
                for content in contents.items():
                    title = content("h3").text()
                    update = content("p").text()
                    comic_url = "http://www.ikanfan.com" + content.attr("href")
                    img = content("div img").attr("data-original")
                    with open("./爱看番.txt", "a+", encoding="utf-8") as f:
                        f.write(title + "\t\t" + update + "\t\t" + comic_url + "\t\t" + img + "\r\n")

        except Exception as e:
            print(e)
        # 暂停休眠几秒
        time.sleep(random.uniform(1, 3))


if __name__ == '__main__':
    get_info()
