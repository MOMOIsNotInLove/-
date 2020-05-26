# -*- coding:utf-8 -*-
import re
import jieba
import numpy as np
import requests
from PIL import Image
from wordcloud import WordCloud
from matplotlib import pyplot as plt

"""
获取哔哩哔哩弹幕
"""


# BV下载页面
def download_page(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        result = requests.get(url=url, headers=headers, timeout=10)
        if result.status_code == 200:
            return result

    except Exception as e:
        print(e)


# 获取cid编码
def get_cid(Bv):
    url = 'https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp'.format(Bv)
    response = download_page(url)
    res_dict = response.json()
    cid = res_dict['data'][0]['cid']
    return cid


# 根据cid请求弹幕
def get_dan_mu(cid):
    url = 'https://api.bilibili.com/x/v1/dm/list.so?oid={}'.format(cid)
    res = download_page(url)
    res_xml = res.content.decode('utf-8')
    pattern = re.compile('<d.*?>(.*?)</d>', re.S)
    dan_mu_list = re.findall(pattern, res_xml)
    return dan_mu_list


# 把弹幕写入到文件中
def save_to_file(dan_mu_list):
    comment_txt = ""
    with open('./{}.txt'.format(bv), mode='w', encoding='utf-8') as f:
        for i in range(len(dan_mu_list)):
            # 将列表中的每个数去除首尾空格后，逐行写入txt文件
            f.write(str(dan_mu_list[i]).strip() + '\n')
            # 拼接成一个字符串
            comment_txt += str(dan_mu_list[i]).strip() + ","


# 弹幕爬虫主流程
def main(bv):
    # 根据视频av号获得cid
    cid = get_cid(bv)
    # 根据cid爬取弹幕
    dan_mu_list = get_dan_mu(cid)
    # 把弹幕写入到文件中
    save_to_file(dan_mu_list)


if __name__ == '__main__':
    bv = str(input("请输入目标BV号：")).strip()
    main(bv)
