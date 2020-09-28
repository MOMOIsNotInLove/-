# -*- coding:utf-8 -*-
import re
import requests
import time

base_url = "http://login.jiayuan.com/?pre_url=%2Fusercp&channel=1&position=21&refrer=http://www.jiayuan.com&host=0"
url = "https://login.jiayuan.com/?channel=200&position=102"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "referer": "https://login.jiayuan.com/err.php?stolen=right&err_type=-14&pre_url=https://usercp.jiayuan.com/"
}
data = {
    "name": "15867119501",
    "password": "chen654321",
    "remem_pass": "on"
}


def get_token():
    try:
        session = requests.session()
        response = session.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            pattern = re.compile('<input type="hidden" name="_s_x_id" value="(.*?)"/>',re.S)
            s_x_id = re.findall(pattern,response.text)
            print(response.text)
            print(s_x_id)
            print(response.cookies)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_token()
