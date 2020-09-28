# -*- coding:utf-8 -*-
import json

import requests
import time
from lxml import etree
from tqdm import tqdm

"""
采集马蜂窝旅游信息：http://www.mafengwo.cn/search/q.php?q={position}&t={choose}&kt=1
position:景点名，比如张家界，九寨沟
choose：查询目标 全部~"" , 商品："sales",游记：”notes“，攻略：”guides“，问答：”questions“
景点：”pois“，酒店：”hotels“，用户：”users“
"""


def get_url():
    position = str(input("请输入查询景点名（比如：张家界）")).strip()
    print("请在如下项目中选择查询类目：全部，商品，游记，攻略，问答，景点，酒店，用户")
    choose = str(input()).strip()
    pages = int(input("请输入查询页数："))
    headers = {
        "Host": "www.mafengwo.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    print("========================")
    for page in range(1, pages + 1):
        try:
            print('\033[5;37;40m正在获取第{}页数据\033[0m'.format(page))
            base_url = "http://www.mafengwo.cn/search/q.php?q={}&p={}&t={}&kt=1".format(position, page, choose)
            response = requests.get(base_url, headers=headers, timeout=5)
            if response.status_code == 200:
                doc = etree.HTML(response.text)
                # 获取所有的节点集
                li_list = doc.xpath(".//div[@class='att-list']/ul/li")
                # 定义一个空数组
                arr_list = []
                for i in li_list:
                    img_url = (i.xpath(".//div[@class='flt1']/a/img/@src")[0]).split("?")[0]
                    name = (i.xpath(".//div[@class='ct-text ']/h3/a/text()")[0]).replace("景点 - ", "")
                    place_url = i.xpath(".//div[@class='ct-text ']/ul/li[1]/a/@href")[0]
                    place = i.xpath(".//div[@class='ct-text ']/ul/li[1]/a/text()")[0]
                    comment_url = i.xpath(".//div[@class='ct-text ']/ul/li[2]/a/@href")[0]
                    comment = i.xpath(".//div[@class='ct-text ']/ul/li[2]/a/text()")[0]
                    notes = i.xpath(".//div[@class='ct-text ']/ul/li[3]/a/text()")[0]
                    print("图片：" + img_url)
                    print("景点名：" + name)
                    print("位置：" + place + "，" + place_url)
                    print("评论：" + comment + "，" + "游记：" + notes + "~：" + comment_url)
                    print("========================")
                    obj = {
                        "景点": name,
                        "位置": place,
                        "评论": comment,
                        "游记": notes,
                        "图片": img_url,
                        "详情": comment_url
                    }
                    arr_list.append(obj)
                    time.sleep(1.2)

                with open("./mafengwo.json", "w", encoding="utf-8") as f:
                    f.write(json.dumps(arr_list,ensure_ascii=False))

        except Exception as e:
            print(e)


if __name__ == '__main__':
    get_url()
