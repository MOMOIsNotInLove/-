# -*- coding:utf-8 -*-
import requests
import pprint

from sign import FANS_API, get_relation_api, get_signed_api

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"


def get_user_followings(uid, cursor=0):
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "referer": "https://www.toutiao.com/c/user/relation/{}/?tab=following".format(uid),
        'user-agent': user_agent,
        'cookie':'csrftoken=5b260d933f14d4957a73512983f36020; ttcid=a83332d66bc24a13a2584d24488a475027; SLARDAR_WEB_ID=6e7b528c-1744-4481-8954-69b88fa6dc9a; s_v_web_id=verify_kcwmu7xt_CpahC8xq_KQVg_49Wp_9CpO_r5t9dVDyaKdX; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6852103945960572423; tt_webid=6852103945960572423; tt_scid=SmD.-pOyBq6XkkqR.nNgLhl5dG1rnTWSoC2QxgQxvEI7uUH7SmpcPVEp9CP-i8.n27f4; __tasessionId=jqvffpxbg1595395392713referer: https://www.toutiao.com/c/user/relation/5954781019/?tab=following',
        "x-requested-with": "XMLHttpRequest",
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'accept': 'application/json,text/javascript'
    }
    try:

        api = get_relation_api(uid, cursor=cursor, user_agent=user_agent)
        response = requests.get(api, headers=headers, timeout=10)
        if response.status_code == 200:
            print(response.text)
        print(response.status_code)
    except Exception as e:
        print(e)


def get_user_fans(uid, cursor=0):
    headers = {
        'cookie': 'tt_scid=CONST',
        'user-agent': user_agent
    }
    api = get_relation_api(uid, cursor=cursor, api=FANS_API, user_agent=user_agent)
    response = requests.get(api, headers=headers)
    print(response.json())


def get_articles(uid, behot_time=0):
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': user_agent,
        "x-requested-with": "XMLHttpRequest",
        "referer": "https://www.toutiao.com/c/user/{}/".format(uid)
    }
    api = get_signed_api(uid, user_agent=user_agent, behot_time=behot_time)
    try:
        response = requests.get(url=api, headers=headers)
        if response.status_code == 200:
            doc = response.json()
            # 获取返回值里的文章data
            data = doc["data"]
            # 获取每一个返回值里的behot_time
            print(data)
            return doc["next"]["max_behot_time"]

    except Exception as e:
        print(e)


if __name__ == '__main__':
    uid = 5954781019
    # get_user_followings(uid)
    # get_user_fans(uid)
    get_articles(uid)
