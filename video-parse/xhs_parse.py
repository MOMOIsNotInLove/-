# -*- coding:utf-8 -*-
import re
import json
import requests
from pyquery import PyQuery as pq

"""
目标APP：小红书
目标url：APP短视频分享链接
爬取思路：
    1. 通过APP里的分享获取视频url：http://xhslink.com/xvxMJ
    2. url重定向到真实跳转地址：简化后.,https://www.xiaohongshu.com/discovery/item/5f77dbcf000000000100491c...
    3. As of 2020-11-04 小红书更新，不再提供无水印接口。且请求头必须携带cookie，才能获取数据
"""


class XiaoHongShu(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def get_video(self):
        headers = {
            "Host": "xhslink.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/79.0.3945.88 Safari/537.36"
        }
        source_headers = {
            "cookie": "xhsTrackerId=6e8cc536-0d57-4226-c27c-831a6e51c4cc; xhsuid=6KOIxzWIclOk5WsI; "
                      "Hm_lvt_d0ae755ac51e3c5ff9b1596b0c09c826=1606207238; "
                      "xhsTracker=url=noteDetail&xhsshare=CopyLink; extra_exp_ids=gif_exp1,ques_exp1; "
                      "timestamp2=20201229ef45ffd4004e2dcc00c97dec; "
                      "timestamp2.sig=a95ob3HUIi0pV4z3n8kQHuJ2sk3HjHT-XdYVwbgEHbs; xhs_spses.5dde=*; "
                      "xhs_spid.5dde=05e7787428e31fd4.1593488621.11.1609225136.1607129499.6465ec57-2e5f-4f43-aaf1"
                      "-161a7fd7a7e6",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/79.0.3945.88 Safari/537.36"
        }
        try:
            # 处理url
            pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',re.S)
            deal_url = re.findall(pattern, self.url)[0]

            # 获取重定向后的简化url
            response = self.session.get(url=deal_url, headers=headers, allow_redirects=False, timeout=10)
            base_url = response.headers.get("Location")

            result = self.session.get(url=base_url, headers=source_headers, timeout=10)
            if result.status_code == 200:
                try:
                    doc = pq(result.text)
                    url = doc("video").attr("src")
                    cover = doc("video").attr("poster")
                    description = doc(".content .as-p").text()
                    info = {
                        "description": description,
                        "cover": "https:" + cover,
                        "url": url
                    }
                    return json.dumps(info, ensure_ascii=False)
                except Exception as e:
                    return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)
            else:
                return json.dumps({"info": "暂无相关数据，请检查相关数据："}, ensure_ascii=False)

        except Exception as e:
            return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)


if __name__ == '__main__':
    redbook = XiaoHongShu("莫邪发布了一篇小红书笔记，快来看吧！😆 NQwY6qKRk6eNrJZ 😆  http://xhslink.com/HInDt，复制本条信息，打开【小红书】App查看精彩内容！")
    print(redbook.get_video())