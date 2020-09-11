# -*- coding:utf-8 -*-
import requests
import json
import time

"""
目标：尝试爬取西瓜视频
"""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "cookie": "td_cookie=2895957341; wafid=aa79e1cd-16dc-421b-b94d-b20a5ebfe91c; wafid.sig=D1-hFWUnCB8JJJTV-R1e_Cdx9uI; ttwid=6828065332000769548; ttwid.sig=ec3MPPdMOxx89J6pbmB2OuU52MA; xiguavideopcwebid=6828065332000769548; xiguavideopcwebid.sig=yjuAl7rEBOyfAgDFXiIB2YRIClg; SLARDAR_WEB_ID=6e7b528c-1744-4481-8954-69b88fa6dc9a; _ga=GA1.2.1690086969.1589782861; _gid=GA1.2.1558373712.1589782861; ixigua-a-s=1; s_v_web_id=verify_kac6yx8v_ow0JbieE_IIBj_41xD_8WKa_oNG1TTArwzeg; _gat_gtag_UA_138710293_1=1"}
url = "https://www.ixigua.com/api/feedv2/feedById?_signature=gr1SjgAgEA1wkmDJc74FlIK9UpAANyM&channelId=94349543909&count=9&maxTime=0&request_from=701"


def get_info():
    try:
        # 获取毫秒级的时间戳
        stamp = int(time.time())
        params = {
            "_signature": "iAhAtAAgEA56J3Lz0Xeki4gIQKAANbX",
            "channelId": "94349543909",
            "count": 9,
            "maxTime": stamp,
            "request_from": 701
        }
        response = requests.get(url=url, timeout=10)
        if response.status_code == 200:
            print(response.json())

    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_info()
