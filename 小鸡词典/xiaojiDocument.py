# -*- coding:utf-8 -*-
import random

import requests
import json
import time

"""
爬取小鸡词典，自定义搜索内容
api搜索目标网址：https://api.jikipedia.com/go/search_definitions
@:param post请求
@:param Request Payload数据格式
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Origin": "https://jikipedia.com/",
    "XID": "xAYJ+2jp7sHGhXQIUdWjzqoLootZvsez9tyRVfeecfyKrjMz98w1vsYWAgAiIh9Eh/aPHRldSRnnGS+vrGSuxXgsagL4yi/Sp2f35tEI0x4=",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "api.jikipedia.com"
}
url = "https://api.jikipedia.com/go/search_definitions"


def get_info(keyWord, pages):
    try:
        for page in range(1, pages + 1):
            params = {
                # 搜索关键字
                "phrase": keyWord,
                # 查询页数
                "page": page
            }
            print("\033[1;31;40m正在打印第%d页数据...\033[0m" % page)
            # 发送post请求
            response = requests.post(url=url, headers=headers, data=json.dumps(params), timeout=10)
            if response.status_code == 200:
                result = response.json()
                """
                通过放回的json数据，可以猜测到利用的是sql分页查询语句：
                select * from table_name 
                limit page,size  
                """
                print("目标搜索总数目：", result["total"])
                print("本页搜索总数目：", result["size"])
                print("起始索引：", result["from"])
                print("终止索引：", result["to"])
                print("当前页数：", result["current_page"])
                print("总页数：", result["last_page"])
                # 循环打印当前页面的内容
                for i in result["data"]:
                    print("===============")
                    print("标题：", i["term"]["title"])
                    print("内容详情：", i["content"])
            time.sleep(random.randint(1,4))
            print("\033[1;32;40m===========================\033[0m")
            print("")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    kw = input("请输入查询关键词：药水哥~~").strip()
    number = int(input("请输入查询页数："))
    get_info(kw, number)
