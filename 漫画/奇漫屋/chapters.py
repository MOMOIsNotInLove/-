# -*- coding:utf-8 -*-
import json
import requests
from pyquery import PyQuery as pq

"""
目标网址：奇漫屋
链接来源：APP链接或web地址
目标地址：http://qiman6.com/22034/
加密原理：
    - 漫画章节大全趋势是分为两部分的，第一部分在网页源代码中
    - 第二部分是点击 “加载更多” 后，发送一个post请求，返回剩余的漫画章节
"""


class QiMan(object):
    def __init__(self, mid):
        """
        返回漫画章节大全
        :param mid: 漫画id
        """
        self.mid = mid
        self.session = requests.Session()

    def parse_html(self):
        url = "http://qiman6.com/{}/".format(self.mid)
        headers = {
            "Host": "qiman6.com",
            "Referer": "http://qiman6.com/{}/".format(self.mid),
            "Upgrade-Insecure-Requests": "1",
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                          "like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 "
        }
        result = self.session.get(url=url, headers=headers, timeout=10)
        if result.status_code == 200:
            try:
                doc = pq(result.text)
                chapters = doc(".catalog-list ul li")
                cover = doc(".box-back1 img").attr("src")
                name = doc(".box-back1 img").attr("title")
                author = (doc(".box-back2 .txtItme").eq(0).text()).split("：")[1]
                category = (doc(".box-back2 .txtItme").eq(1).text()).split("：")[1]
                info = {
                    "name": name,
                    "author": author,
                    "cover": cover,
                    "category": category
                }
                items = []
                for row in chapters.items():
                    items.append({
                        "id": row.attr("data-id"),
                        "name": row("a").text()
                    })
                return items, info, name
            except Exception as e:
                return json.dumps({"error": str(e)}, ensure_ascii=False)

    def parse_api(self):
        headers = {
            "Host": "qiman6.com",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/84.0.4147.125 Safari/537.36 "
        }
        response = self.session.post(url="http://qiman6.com/bookchapter/", headers=headers,
                                     data="id={}&id2=1".format(self.mid), timeout=10)
        if response.status_code == 200:
            try:
                return response.json()
            except Exception as e:
                return json.dumps({"error": str(e)}, ensure_ascii=False)
        else:
            return json.dumps({"status": response.status_code}, ensure_ascii=False)


if __name__ == '__main__':
    mid = "22034"
    qi_man = QiMan("22034")
    list1, msg, title = qi_man.parse_html()
    list2 = qi_man.parse_api()
    arr = list(list1)+(list(list2))
    with open("./chapters-{}.json".format(title), "w", encoding="utf-8") as f:
        f.write(json.dumps({"message": msg, "data": arr}, ensure_ascii=False))
