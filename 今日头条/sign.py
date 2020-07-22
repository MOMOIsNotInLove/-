# -*- coding:utf-8 -*-
import os
from as_cp import get_as_cp


ARTICLE_API = "https://www.toutiao.com/toutiao/c/user/article/?page_type=1&user_id={uid}&max_behot_time={mbt}&count=20&as={_as}&cp={_cp}"
FOLLOWING_API = "https://www.toutiao.com/toutiao/c/user/following/?user_id={uid}&cursor={cursor}&count=20"
FANS_API = "https://www.toutiao.com/toutiao/c/user/followed/?user_id={uid}&cursor={cursor}&count=20"


def get_signed_api(uid, user_agent, behot_time=0):
    ascp = get_as_cp()
    _as = ascp['as']
    _cp = ascp['cp']
    api = ARTICLE_API.format(
        uid=uid,
        mbt=behot_time,
        _as=_as,
        _cp=_cp
    )
    result = os.popen('node sign.js "{}" "{}"'.format(api, user_agent))
    signature = result.read().strip()
    article_url = api+"&_signature={}".format(signature)
    return article_url


def get_relation_api(uid, user_agent, cursor=0, api=FOLLOWING_API):
    url = api.format(uid=uid, cursor=cursor)
    result = os.popen('node sign.js "{}" "{}"'.format(api, user_agent))
    sign = result.read().strip()
    relation_url = f'{url}&_signature={sign}'
    return relation_url


# if __name__ == '__main__':
#     uid = '5954781019'
#     user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
#     print(get_signed_api(uid=uid, user_agent=user_agent))
