# -*- coding:utf-8 -*-
import requests
import json
import re

"""
目标APP：抖音火山版
目标url：APP视频分享链接
爬取思路：
    1. 很失败，一直没有找到无水印的api，只能分析出带水印的
    2. 机缘巧合，发现一篇csdn文章：https://blog.csdn.net/qq_44700693/article/details/108089085
    
       - https://api-hl.huoshan.com/hotsoon/item/video/_source/?item_id=6859730122820291840 原火山小视频无水印接口
       - https://api.huoshan.com/hotsoon/item/video/_reflow/?item_id=6859730122820291840 抖音火山版水印接口
       - https://api.huoshan.com/hotsoon/item/video/_source/?item_id=6859730122820291840 抖音火山版无水印接口
    3. item_id为APP分享的链接跳转后的url查询字符串
"""


class HuoShan(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def get_video(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/85.0.4183.102 Safari/537.36 "
        }
        try:
            # 处理url,获取视频id
            pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.S)
            deal_url = re.findall(pattern, self.url)[0]
            response = self.session.get(url=deal_url, headers=headers, timeout=10)
            # 获取重定向后的简化url
            base_url = response.url
            # 获取跳转url中的item_id
            item_id = re.findall("item_id=(\d+)&",base_url,re.S)[0]
            api = "https://api.huoshan.com/hotsoon/item/video/_source/?item_id={}".format(item_id)
            result = self.session.get(url=api, headers=headers, timeout=10)
            if result.status_code == 200:
                try:
                    info = {
                        "video_url": result.url,
                        "description": "因api接口问题，获取用户/封面较麻烦，故暂时仅开放视频链接"
                    }

                    return json.dumps(info, ensure_ascii=False)
                except Exception as e:
                    return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)
            else:
                return json.dumps({"info": "暂无相关数据，请检查相关数据："}, ensure_ascii=False)

        except Exception as e:
            return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)


if __name__ == '__main__':
    huoshan = HuoShan("文文🌸🌸🌸在火山分享了视频，快来围观！传送门戳我>>https://share.huoshan.com/hotsoon/s/9p5kq9ObEc8/ 复制此链接，打开【火山极速版】，直接观看视频~")
    print(huoshan.get_video())
