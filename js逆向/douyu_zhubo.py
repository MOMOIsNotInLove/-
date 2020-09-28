import sys
import os
import json

import jsonpath
import requests
from pyquery import PyQuery as pq


# 创建一个实例对象
class DouYuSpider(object):
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_html(self):

        try:
            html = requests.get(self.url, self.headers)
            if html.status_code == 200:
                return html.json()
            return None
        except Exception as e:
            print(e)


    def get_data(self, html):
        """"
        jsonpath使用说明：jsonpath(标准json数据格式，提取规则)是另一种提取json数据的方法
        "$..on":含义是从根节点出发，遍历全局，找到键名为“on”的所有数据，将所有的值存储到一个列表中
        $表示当前页面,也可以理解为全局页面，根节点
        ..:表示子孙节点
        on：表示json的键名为“on”
        """
        names = jsonpath.jsonpath(html, "$..nn")
        values = jsonpath.jsonpath(html, "$..ol")
        # 构建一个字典
        items = []
        for name, value in zip(names, values):
            item = {
                "name": name,
                "value": value
            }
            # 利用一个生成器
            items.append(item)
        print(items)

    def go(self):
        html = self.get_html()
        self.get_data(html)


if __name__ == '__main__':
    url = "https://www.douyu.com/gapi/rkc/directory/2_1/1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    douYuSpider = DouYuSpider(url, headers)
    douYuSpider.go()
