# -*- coding:utf-8 -*-
import os
import time
import re
import requests
import json
import random

from tqdm import tqdm

"""
腾讯QQ音乐爬取练习

@:params 专辑url相关

专辑列表url：https://c.y.qq.com/soso/fcgi-bin/client_search_cp?t=8&p=1&n=10&w=周杰伦&format=json


@:param 单曲url相关
 原来的url很长，经过删选一些无用的请求参数，缩减为：
搜索url： https://c.y.qq.com/soso/fcgi-bin/client_search_cp?new_json=1&cr=1&catZhida=1&p=1&n=10&w=一路向北&format=json&inCharset=utf8
评论url： https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?biztype=1&topid=106291297&cmd=8&pagenum=0&pagesize=25
歌曲下载url1： http://180.153.119.143/amobile.music.tc.qq.com/C400{获取的播放列表的mid}.m4a?guid={guid，固定值}&vkey={另一个url返回的vkey值}&uin=4689&fromtag=66
歌曲下载url2： http://isure.stream.qqmusic.qq.com/C400{获取的播放列表的mid}.m4a?guid={guid，固定值}&vkey={另一个url返回的vkey值}&uin=4689&fromtag=66
获取vkey的url（即下面展示的新旧两个api）


解析加密参数:通过博客（https://blog.csdn.net/weixin_44119390/article/details/90812246）发现，

到目前2020-06-04为止，其实现在的QQ音乐网站已经相比于文章描述的时候已经改版。
+ 现在有两个API接口：
    1.文章所提及的API（https://u.y.qq.com/cgi-bin/musicu.fcg）接口，请求方式为【GET】,请求参数也只有data部分【至今可用】
    2.新版的API已经变为（https://u.y.qq.com/cgi-bin/musics.fcg），请求方式为【GET】,请求参数必须包含sign和data部分

+ 参数说明：
   + guid：唯一值，与每一个账户相绑定
   + mid = 每一首歌曲的唯一标识id
   + uin = 唯一值，应该为账户名

+ 腾讯QQ音乐爬虫的流程示意：
   1. 先通过搜索API或其它方式获取每一首歌曲的mid（形如 004GNa6e1ze5dk）
   2. 通过新旧API获取vkey，为了拼接成最后的音频url
   3. 遍历下载歌曲    
"""

session = requests.Session()
keyword = input("请输入查询QQ音乐内容：")
pages = int(input("查询QQ音乐页数："))


def get_music():
    url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp"
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "origin": "https://y.qq.com",
        "referer": "https://y.qq.com/portal/search.html",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }

    music_lists = []
    for page in range(1, pages + 1):
        params = {
            "new_json": "1",
            "cr": "1",
            "catZhida": "1",
            # 页数
            "p": page,
            # 偏移量
            "n": 10,
            "w": keyword,
            "format": "json",
            "inCharset": "utf8"
        }
        try:
            response = session.get(url, headers=headers, params=params, timeout=10)
            if response.status_code == 200:
                # 返回相关歌曲内容
                music_lists.append(parse_music(response.json()))
        except Exception as e:
            print(e)
    return music_lists


def parse_music(result):
    """
    解析返回的json数据
    :return: 每一首歌曲的播放url
    """
    # 获取歌曲列表数组集
    datas = result["data"]["song"]["list"]
    # 初始化一个空列表用来保存每一页的歌曲列表
    music_array = []
    for data in datas:
        title = data["title"]
        subtitle = data["subtitle"]
        time_public = data["time_public"]
        singer = data["singer"][0].get("name")
        id = data["id"]
        mid = data["mid"]
        """
        id和mid很重要：
            id用于构建获取用户评论的url
            mid用于构建歌曲播放详情页面的url
        """
        # print("================")
        # print("title：", title)
        # print("subtitle：", subtitle)
        # print("time_public：", time_public)
        # print("singer：", singer)
        # print("id：", id)
        # print("mid：", mid)
        # print("")
        music_array.append({
            "id": id,
            "mid": mid,
            "title": title,
            "subtitle": subtitle,
            "time_public": time_public,
            "singer": singer,
        })
    # 返回列表
    return music_array


# 腾讯QQ音乐老版API接口（可用）
def parse_js_old(guid, mid, uin):
    """
    存在一个问题为解决：对于一些歌曲会弹出 ”您播放的歌曲仅限客户端播放“ ，这时我们就需要以移动端的方式访问
    :param guid:
    :param mid:
    :param uin:
    :return:
    """
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "origin": "https://y.qq.com",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    keyUrl = 'https://u.y.qq.com/cgi-bin/musicu.fcg?&data={"req":{"param":{"guid":" %s"}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"%s","songmid":["%s"],"uin":"%s"}},"comm":{"uin":%s}}' % (
        guid, guid, mid, uin, uin)
    res = session.get(url=keyUrl, headers=headers)
    html = res.text
    keyjs = json.loads(html)
    purl = keyjs['req_0']['data']['midurlinfo'][0]['purl']
    # 拼接成最终的mp3访问url
    url = "http://isure.stream.qqmusic.qq.com/" + purl
    return url


# 新版API接口（未完成解析js的sign加密，待完成）
def parse_js(sign, guid, mid, uin):
    """
    :param sign:js加密参数，时刻变化
    :param guid:guid是登录后才能获取，好像每一个QQ都是唯一值，我的参数好像是7238047136
    :param mid:之前获取mid参数
    :param uin:登录之后的才能获取的参数，好像是QQ号码
    :return: m4a歌曲url
    """
    url = "https://u.y.qq.com/cgi-bin/musics.fcg"
    params = {
        # sign 是js加密，时刻变化
        "sign": sign,
        "data": '{"req_0":{'
                '"module":"vkey.GetVkeyServer",'
                '"method":"CgiGetVkey",'
                '"param":{'
                '"guid":"{0}",'
                '"songmid":["{1}"],'
                '"songtype":[0],'
                '"uin":"{2}",'
                '"loginflag":1,'
                '"platform":"20"}},'
                '"comm":{"uin":{3},"format":"json","ct":24,"cv":0}}'.format(guid, mid, uin, uin)
    }
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "origin": "https://y.qq.com",
        "sec-fetch-mode": "cors",
        "referer": "https://y.qq.com/portal/player.html",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    response = session.get(url, headers=headers, params=params, timeout=10)
    if response.status_code == 200:
        res = response.json()
        purl = res['req_0']['data']['midurlinfo'][0]['purl']
        return purl


# 解析移动端的mp3的url
def parse_js_m(mid):
    # 每一首歌曲播放界面的url
    play_url = "https://i.y.qq.com/v8/playsong.html?songmid={}".format(mid)
    headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "sec-fetch-mode": "navigate",
        "upgrade-insecure-requests": "1"
    }
    info = session.get(url=play_url, headers=headers, timeout=10)
    if info.status_code == 200:
        doc = info.text
        # 正则提取MP3播放url
        pattern = re.compile('<audio id="h5audio_media" height="0" width="0" src="(.*?)" autoplay></audio>', re.S)
        m_url = re.findall(pattern, info.text)[0]
        return m_url


# PC端开始下载歌曲
def download_music(url, title, singer):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    byte = session.get(url, headers=headers, stream=True)
    # 检查文件路径是否存在
    path = "./歌曲下载/{}".format(keyword)
    if not os.path.exists(path):
        os.makedirs(path)
    # 开始下载
    with open(path + "/{}-{}.m4a".format(title, singer), "wb") as f:
        f.write(byte.content)


def start():
    guid = "7238047136"
    uin = "3434279505"
    # 遍历数组数据
    for music_pages in get_music():
        for item in music_pages:
            mid = item.get("mid")
            title = item.get("title")
            singer = item.get("singer")
            print("正在下载：《{}》--{}--{}".format(title, singer,mid))
            print("")
            url = parse_js_old(guid, mid, uin)
            """
            这里很重要：但我们无法获取url时，就要思考一下是不是弹出“您播放的歌曲仅限客户端播放”
            这时我们就要利用移动端的方式请求
            """
            if url is None:
                # 移动端的方式获取下载url
                url = parse_js_m(mid)
            # 开始下载
            download_music(url, title, singer)
            time.sleep(random.uniform(1, 3))


if __name__ == '__main__':
    # parse_js_old("7238047136", "0039MnYb0qxYhV", "3434279505")
    start()
