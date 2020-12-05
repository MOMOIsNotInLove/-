# -*- coding:utf-8 -*-
import json
import js2py
import requests
from pyquery import PyQuery as pq

"""
目标网址：奇漫屋
链接来源：漫画具体章节
目标地址：http://qiman6.com/11557/1204610.html
加密原理：
    - script标签里存在加密图片
    - 采用js的eval加密，需要使用js2py模块来处理eval
"""


def execute_js(comic_id, chapter_id):
    api = "http://qiman6.com/{}/{}.html".format(comic_id, chapter_id)
    headers = {
        "Host": "qiman6.com",
        "Referer": "http://qiman6.com/{}/".format(comic_id),
        "Upgrade-Insecure-Requests": "1",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                      "like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 "
    }
    result = requests.get(url=api, headers=headers, timeout=10)
    if result.status_code == 200:
        try:
            doc = pq(result.text)
            html = doc("body script").eq(0).text()
            images = js2py.eval_js(html)
            return json.dumps(list(images), ensure_ascii=False)
        except Exception as e:
            return json.dumps({"error": str(e)}, ensure_ascii=False)


if __name__ == '__main__':
    print(execute_js("11557", "1204610"))
