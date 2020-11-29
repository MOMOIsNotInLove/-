# -*- coding:utf-8 -*-
import re
import json
import random
import requests

"""
目标APP：哔哩哔哩
目标url：APP视频分享链接或web地址
爬取思路：
    1、模拟手机端请求，视频链接就添加在源码中。（最简单、但清晰度不好）
    2、通过调用别人的接口来下载视频。（根据接口的破解难度而定，可选择清晰度，不过最高的清晰度仅为未登录时能观看的最大清晰度）
    3、直接通过B站的网页版来抓取。（难度稍大，不过清晰度很好，有大会员的话，能下载4K视频）
"""


class BiLiBiLi(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.headers = {
            'Range': 'bytes=0-',
            'referer': self.url,
            'origin': 'https://www.bilibili.com/',
            # 'cookie':'填写自己的B站大会员cookie',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63 '
        }

    def parse(self):
        try:
            rows = self.session.get(url=self.url, headers=self.headers, timeout=10)
            if rows.status_code == 200:
                html = rows.text
                json_data = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
                video_name = re.findall('name="description" content="(.*?)">', html, re.S)[0]
                cover = re.findall('property="og:image" content="(.*?)">', html, re.S)[0]
                if video_name == '':
                    video_name = int(random.random() * 2 * 1000)
                video = json.loads(json_data)['data']['dash']['video'][0]['baseUrl']
                audio = json.loads(json_data)['data']['dash']['audio'][0]['baseUrl']
                """
                self.download(video, "./" + video_name + '.flv')    # 视频保存下载
                为什么文件格式保存为flv格式，而不是选择mp4？
                    默认是下载分辨率最高的，而b站api的返回值中的提到过这样一句话:
                       - "accept_format":"hdflv2,flv,flv720,flv480,mp4"
                       - 测试下载为mp4格式，感觉也没差🙃🙃🙃
                """
                info = {
                    "title": video_name,
                    "cover": cover,
                    "video": video,
                    "audio": audio,
                    "notes": "B站音视频是分开的，并且链接具有时效性，且播放格式是flv的"
                }
                return json.dumps(info, ensure_ascii=False)
            else:
                return json.dumps({"info": "暂无相关数据，返回状态码：" + str(rows.status_code)}, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)

    def download(self, url, save_path):
        """
        将m4s格式保存到本地
        :param url: 视频真实url地址
        :param save_path: 文件保存路径
        :return: None
        """
        response = requests.get(url, headers=self.headers)
        with open(save_path, 'wb') as f:
            f.write(response.content)


class BiLiPhone(object):
    def __init__(self, bv):
        self.bv = bv
        self.session = requests.Session()

    def get_url(self):
        url = self.bv
        if len(url) >= 16:
            base_url = url
        else:
            base_url = "https://m.bilibili.com/video/" + str(self.bv)
        headers = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, "
                          "like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 "
        }

        try:
            response = self.session.get(url=base_url, headers=headers, timeout=5)
            if response.status_code == 200:
                pattern = re.compile("options = \{(.*?)\}", re.S)
                try:
                    res = re.findall(pattern, response.text)[0]
                    readyDuration = re.findall("readyDuration: (.*?),", res)[0]
                    bvid = re.findall("bvid: '(.*?)',", res)[0]
                    readyPoster = re.findall("readyPoster: '(.*?)',", res)[0]
                    readyVideoUrl = re.findall("readyVideoUrl: '(.*?)',", res)[0]
                    rows = {
                        "bvid": bvid,
                        "cover": "https:" + readyPoster,
                        "video_url": "https:" + readyVideoUrl,
                        "duration": readyDuration
                    }
                    return json.dumps(rows, ensure_ascii=False)
                except Exception as e:
                    return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)
            else:
                return json.dumps({"info": "暂无相关数据，请检查相关数据："}, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)


def core():
    print('*' * 10 + '\t BiLiBiLi视频下载\t' + '*' * 10)
    print('*' * 5 + "\t\tAuthor: BadWoman\t\t" + '*' * 5)
    share_url = input('请输入分享链接: ')
    deal_url = re.findall('(http[s]?://[^\s]+)', share_url, re.S)[0]
    choice = int(input("1、模拟手机端下载  2、调用接口下载  3、直接下载\n选择下载方式："))
    if choice == 1:
        return BiLiPhone(deal_url).get_url()
    if choice == 2:
        return "暂无，西蒂蒙"
    if choice == 3:
        return BiLiBiLi(deal_url).parse()


if __name__ == '__main__':
    print(core())