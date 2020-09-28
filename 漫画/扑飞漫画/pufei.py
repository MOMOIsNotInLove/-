# -*- coding:utf-8 -*-
import os
import re
import execjs
import requests
from pyquery import PyQuery as pq
from tqdm import tqdm

headers = {
    "Host": "www.pufei8.com",
    "Referer": "http://www.pufei8.com/",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': "1",
    "User-Agent": "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.9.168 Version/11.52"
}


def get_comic_list(source):
    # 构建新的js加密源码
    result = "function getComic(){" + source + "return photosr.slice(1);}"
    # url：http://res.img.fffmanhua.com/images/2020/07/21/01/47e2cb389f.png/0
    ctx = execjs.compile(result)
    return ctx.call("getComic")


def get_source():
    url = "http://www.pufei8.com/manhua/{}/".format(uid)

    try:
        response = requests.get(url, headers=headers, timeout=10, allow_redirects=False)
        if response.status_code == 200:

            # 源网页的编码格式为gb2312，故重新设置编码格式
            response.encoding = "GBK"
            # pyquery初始化
            html = pq(response.text)
            doc = html("#section  div ul  li a")
            comic_list = []
            for i in doc.items():
                obj = {"title": i.text(), "links": "http://www.pufei8.com" + i.attr("href")}
                comic_list.append(obj)
            # 数组转换
            comic_list.reverse()
            print(comic_list)
            return comic_list
        else:
            print("User-Agent已过期，请及时更换")
            return None

    except Exception as e:
        print(e)


def get_image():
    # 这里举例说明，取其中第一个数
    """
    这里可以对数组进行设计：起始索引，截止索引，这样就可以取出我们想要的数据段
    """
    comic_list = get_source()
    url = comic_list[1].get("links")
    name = comic_list[1].get("title")
    try:
        response = requests.get(url=url, headers=headers, timeout=10)
        if response.status_code == 200:
            # 源网页的编码格式为gb2312，故重新设置编码格式
            response.encoding = "GBK"
            pattern = re.compile('<script language="javascript" type="text/javascript">(.*?)</script>', re.S)
            source = re.findall(pattern, response.text)[0]
            # eval解密,并返回每一章节的解密图片数组
            results = get_comic_list(source)
            return results, name

    except Exception as e:
        print(e)


def download():
    rows, name = get_image()
    path = "./pufei/漫画id-{}/{}/".format(uid, name)
    if not os.path.exists(path):
        os.makedirs(path)
    for index in tqdm(range(len(rows))):
        url = "http://res.img.fffmanhua.com/" + rows[index]
        response = requests.get(url, stream=True)
        with open(path + str(index) + ".png", 'wb') as f:
            f.write(response.content)


if __name__ == '__main__':
    uid = int(input("请输入查询漫画的编号：e.g:8 :").strip())
    download()
