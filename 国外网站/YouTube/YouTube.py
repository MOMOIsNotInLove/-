# -*- coding:utf-8 -*-
import re
import json
import requests
from urllib import parse

"""
目标网址：YouTube单视频下载
链接来源：APP分享链接或web地址
目标地址：api-> https://www.youtube.com/watch?v=QBjKntYuUIk
加密原理：
    - 访问目标api：获取网页源代码
    - 真实的视频地址在网页源代码的args中
    - 天坑：你在浏览器中打开YouTube时和你用程序访问YouTube时，得到的网页源代码天差地别，html样式完全不同
        - 怀疑点：有没有可能是没有携带headers中的x-client-data参数，但这个参数十分复杂，加密方式很怪
        - 我是将程序返回的源代码粘贴到一个html文件中，格式化后，发现两者完全不一样
"""


class YouTube(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def parse(self):
        # 处理url
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.S)
        deal_url = re.findall(pattern, self.url)[0]
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/85.0.4183.102 Safari/537.36"
        }
        pattern = re.compile('"formats":\[(.*?)\],', re.S)
        pattern_detail = re.compile('"videoDetails":\{(.*?)\},"', re.S)
        try:
            response = self.session.get(url=deal_url, headers=headers, timeout=30)
            if response.status_code == 200:
                res = response.text
                html = re.findall(pattern, res)[0]
                doc = json.loads("[" + html + "]")
                video_url = doc[-1]["url"]
                quality = doc[-1]["qualityLabel"]
                # 处理播放明细
                detail = json.loads("{" + re.findall(pattern_detail, res)[0] + "}}")
                info = {
                    "title": detail["title"],
                    "lengthSeconds": detail["lengthSeconds"],
                    "quality": quality,
                    "cover": detail["thumbnail"]["thumbnails"][-1]["url"],
                    "url": parse.unquote(video_url)
                }
                return json.dumps(info, ensure_ascii=False)
            return json.dumps({"status": response.status_code}, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"error": str(e)}, ensure_ascii=False)


if __name__ == '__main__':
    youtube = YouTube("https://www.youtube.com/watch?v=QBjKntYuUIk")
    print(youtube.parse())