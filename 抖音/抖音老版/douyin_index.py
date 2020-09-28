# -*- coding:utf-8 -*-
import json
import requests
import re

"""
解析抖音视频的_signature
1. headers一律使用移动端的user-agent
2. 解析详细文章参考： https://mp.weixin.qq.com/s/3r8yVDZ0lKrgot3XV6-8cA
"""
user_id = "102777167489"

# 第一次请求，利用会话来请求
url = "https://www.iesdouyin.com/share/user/{}".format(user_id)
headers = {
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}

session = requests.Session()
res = session.get(url, headers=headers, timeout=10)

# 正则提取dytk
pattern = re.compile("dytk: '(.*?)'", re.S)
dytk = re.findall(pattern, res.text)[0]
print(dytk)  # 373c0c83cf5a69b82a5264f3482103d9

# 正则提取tac
pattern = re.compile("<script>tac='(.*?)'</script>", re.S)
tac = re.findall(pattern, res.text)[0]
print(tac)

# 休眠30秒，方便输入signature
signature = input("请输入signature:")

headers1 = {
    ":authority": "www.iesdouyin.com",
    ":method": "GET",
    ":scheme": "https",
    "accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cookie": "_ga=GA1.2.539821167.1590025995; _gid=GA1.2.910016359.1590025995",
    "referer": "https://www.iesdouyin.com/share/user/{}".format(user_id),
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "x-requested-with": "XMLHttpRequest",
}
# 第二次请求
params = {
    "user_id": user_id,
    "sec_uid": "",
    "count": 21,
    "max_cursor": 0,
    "aid": 1128,
    "_signature": signature,
    "dytk": dytk
}
base_url = "https://www.iesdouyin.com/web/api/v2/aweme/post/"
# 解析返回json值
response = session.get(base_url, headers=headers, params=params, timeout=10)
print(json.loads(response.text))
