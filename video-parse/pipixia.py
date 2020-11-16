# -*- coding:utf-8 -*-
import re
import json
import requests


"""
目标APP：皮皮虾
目标url：APP短视频分享链接
爬取思路：
    1. 通过APP里的分享获取视频url：https://h5.pipix.com/s/JAtW8Yg/
    2. url重定向到真实跳转地址：简化后.,https://h5.pipix.com/item/6869230768778909965
    3. 获取重定向后的url的item_id,携带其发送get请求
    4. As of 10/20/2020, 皮皮虾app更新了接口不再暴露无水印视频地址
奇怪点：
    1. 任意分享的视频链接如下：
       - https://h5.pipix.com/s/3asShh（✅）
       - https://h5.pipix.com/s/JRjEVyT（✖）
       - https://h5.pipix.com/s/JAtW8Yg（✖）
       - https://h5.pipix.com/s/rR5Ppu（✅）
    2. 发现有些视频链接，获取访问结果的json中的“comment”字段里居然藏有无水印的视频url
    3. 有些分享链接的comment字段为空数组，有些又有值。想通过app分享链接百分百拿到无水印视频url感觉有点困难，除非知道内部视频数据api
"""


class PiPiXia(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def parse(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/85.0.4183.102 Safari/537.36"
        }
        share_headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/86.0.4240.193 Safari/537.36 "
        }
        try:
            response = self.session.get(url=self.url, headers=headers, timeout=10)
            # 获取重定向后的简化url
            base_url = str(response.url).strip().split("?app")[0]
            # 获取视频id
            pattern = re.compile("/(\d+)", re.S)
            vid = re.findall(pattern, base_url)[0]
            # get请求视频地址
            api = "https://h5.pipix.com/bds/webapi/item/detail/?item_id={}&source=share".format(vid)
            result = self.session.get(url=api, headers=share_headers, timeout=10)
            if result.status_code == 200:
                try:
                    res = result.json()
                    title = res["data"]["item"]['content']
                    # 判断comments是否为空
                    if len(res["data"]["item"]['comments']) > 0:
                        # comment里面才是真正的无水印视频地址
                        url = res["data"]["item"]['comments'][0]['item']['video']['video_high']['url_list'][0]['url']
                    else:
                        # 去有水印的视频地址
                        url = res["data"]["item"]["video"]["video_download"]["url_list"][0]["url"]
                    name = res["data"]["item"]["author"]["name"]
                    cover = res["data"]["item"]["cover"]["url_list"][0]["url"]
                    description = res["data"]["item"]["author"]["description"]
                    info = {
                        "title": title,
                        "name": name,
                        "description": description,
                        "cover": cover,
                        "video_url": url
                    }
                    return json.dumps(info, ensure_ascii=False)
                except Exception as e:
                    return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)
            else:
                return json.dumps({"info": "暂无相关数据，请检查相关数据："}, ensure_ascii=False)

        except Exception as e:
            return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)


if __name__ == '__main__':
    pi_pi = PiPiXia("https://h5.pipix.com/s/3asShh")
    # pipi = PiPiXia("https://h5.pipix.com/s/rR5Ppu")
    # pipi = PiPiXia("https://h5.pipix.com/s/JRjEVyT")
    # pipi = PiPiXia("https://h5.pipix.com/s/JAtW8Yg")
    print(pi_pi.parse())
