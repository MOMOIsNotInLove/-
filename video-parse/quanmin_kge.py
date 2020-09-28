# -*- coding:utf-8 -*-
import requests
import json
import re

"""
目标APP：全名K哥
目标url：视频分享链接
"""


class KGe(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def get_video(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/85.0.4183.102 Safari/537.36 "
        }
        try:
            result = self.session.get(url=self.url, headers=headers, timeout=10)
            pattern = re.compile('"playurl_video":"(.*?)",', re.S)
            if result.status_code == 200:
                try:
                    res = result.text
                    url = re.findall(pattern, res)[0]
                    info = {
                        "url": url,
                    }
                    return json.dumps(info, ensure_ascii=False)
                except Exception as e:
                    return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)
            else:
                return json.dumps({"info": "暂无相关数据，请检查相关数据："}, ensure_ascii=False)

        except Exception as e:
            return json.dumps({"info": "暂无相关数据，请检查相关数据：" + str(e)}, ensure_ascii=False)


if __name__ == '__main__':
    kuaishou = KGe(
        "https://kg2.qq.com/node/play?s=D8Gr_IDswJgotDe9&shareuid=&topsource=a0_pn201001006_z11_u3080405925_l1_t1601294577__")
    print(kuaishou.get_video())
