# -*- coding:utf-8 -*-
import random
import time
from tqdm import tqdm
import requests
from pyquery import PyQuery as pq

"""
获取SF互动传媒网的轻小说大全
@:param url：http://book.sfacg.com/List/default.aspx
@:param tid: get请求参数的作品类别
    -1：全部  21：魔幻  22：玄幻
    23：古风  24：科幻  25：校园
    26：都市  27：游戏  28：同人
    29：悬疑   
    
@:param if:get请求参数的写作进度
    2：不限 0：连载中 1：已完结
    
@:param ud：get请求参数的更新时间
    -1：不限 7：七日内  15:半月内  30：一个月内

@:param PageIndex:get请求的页数参数

@:return txt整理文档
"""

url = "http://book.sfacg.com/List/default.aspx"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "book.sfacg.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}


def get_info():
    start_page = int(input("请输入查询起始页码："))
    pages = int(input("请输入查询页数："))
    for page in tqdm(range(start_page, pages + 1)):
        params = {
            "tid": "-1",
            "if": "2",
            "ud": "-1",
            "PageIndex": page
        }
        try:
            response = requests.get(url=url, headers=headers, params=params, timeout=10)
            if response.status_code == 200:
                # pyquery初始化字符
                doc = pq(response.text)
                # 获取遍历ul标签大全
                contents = doc(".bsubcon .Blue_link3 ul")
                for content in contents.items():
                    book_url = "http://book.sfacg.com" + content.find("li").eq(0)("a").attr("href")
                    img = content.find("li").eq(0)("a img").attr("src")
                    words = content.find("li").eq(1).text()
                    title = words.split("\n")[0]
                    author = (words.split("\n")[1])[5:]
                    info = words.split("\n")[2]
                    introduction = words.split("\n")[3]
                    with open("./轻小说.txt", "a+", encoding="utf-8") as f:
                        f.write(
                            title + "\t\t" + author + "\t\t" + book_url + "\t\t" + img + "\t\t" + info + "\t\t" + introduction + "\r\n")

        except Exception as e:
            print(e)
        # 暂停休眠几秒
        time.sleep(random.uniform(1, 3))


if __name__ == '__main__':
    get_info()
