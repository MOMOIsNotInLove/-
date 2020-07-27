# -*- coding:utf-8 -*-
import requests
from pyquery import PyQuery as pq
import time
from tqdm import tqdm


def get_urls(url):
    # 采取自己的博客所有的文章的url以及标题
    base_url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    try:
        response = requests.get(url=base_url, headers=headers, timeout=10)
        if response.status_code == 200:
            # 进行pyquery初始化
            doc = pq(response.text)
            html = doc(".article-item-box h4 a")
            # 统计采集的样本个数
            number = 0
            # 遍历目标每一个节点
            for item in html.items():
                url = item.attr("href")
                title = item.text()
                title = title.replace("原创", "").replace("转载", "").strip()
                number += 1
                print("\033[1;41;42m{}：\033[0m".format(title), url)
            print("\033[0;41m采集总数目：\033[0m", number)
    except Exception as e:
        print(e)


def get_page():
    pages = int(input("请输入查询页数："))
    target_url = str(input("请输入查询博主主页id(比如 qq_45351802)：")).strip()
    for page in tqdm(range(1, pages + 1), ncols=80):
        csdn_url = "https://blog.csdn.net/" + target_url + "/article/list/" + str(page)
        get_urls(csdn_url)
        # 设置休眠时间，减缓爬取速度
        time.sleep(6)


def get_content():
    pass


if __name__ == '__main__':
    get_page()
