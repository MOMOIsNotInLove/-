# -*- coding:utf-8 -*-
import os
import random
import re
import time
import demjson
import requests
import execjs
from urllib import parse
from pyquery import PyQuery as pq
from tqdm import tqdm


# 获取漫画列表大全
def get_comic_list():
    url = "https://www.zymk.cn/nodeapi/comic/allComic/"
    headers = {
        "referer": "https://www.zymk.cn/sort/all.html",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            # 获取返回的json数据
            result = response.json()["data"]
            # 截取前100组数据就行了
            for i in tqdm(iterable=result[0:100], desc="知音漫客："):
                comic_id = i["comic_id"]
                comic_name = i["comic_name"]
                last_id = i["last_chapter"]["id"]
                last_name = i["last_chapter"]["name"]
                da_shang = i["dashang"]
                pingfen = i["pingfen"]
                total_click = i["total_click"]
                update_time = i["update_time"]
                zongpiao = i["zongpiao"]
                print("")
                print("漫画名：", comic_id)
                print("漫画id", comic_name)
                print("最近更新章节名：", last_name)
                print("最近更新章节id：", last_id)
                print("更新时间：", update_time)
                print("打赏：", da_shang)
                print("评分：", pingfen)
                print("点击量：", total_click)
                print("总票：", zongpiao)
                print("======================")
                time.sleep(1.5)
    except Exception as e:
        print(e)


# 获取某部具体的漫画章节大全
def get_comic():
    comic_id = input("请输入漫画id编号：").strip()
    url = "https://www.zymk.cn/{}".format(comic_id)
    headers = {
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "upgrade-insecure-requests": "1"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            # pyquery初始化返回的网页数据
            result = pq(response.text)
            # 获取漫画章节的li大全
            html = result("#chapterList li")
            # 漫画章节列表
            comic_array = []
            # 漫画总章节数
            number = len(html)
            # pyquery多节点遍历时，一定要使用.items()方法
            for item in html.items():
                obj = {"url": "https://www.zymk.cn/{}/".format(comic_id) + item("a").attr("href"),
                       "title": item("a").text()}
                comic_array.append(obj)
            # 将漫画列表按照升序排列 .reverse()方法没有返回值
            comic_array.reverse()
            return comic_array, number
    except Exception as e:
        print(e)


# 开始下载漫画
def get_images(comic_url):
    headers = {
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "upgrade-insecure-requests": "1"
    }
    try:
        response = requests.get(url=comic_url, headers=headers, timeout=10)
        if response.status_code == 200:
            doc = pq(response.text)
            # 获取每一章节的图片核心加密js代码
            core_code = doc("#content .comiclist script")
            pattern = re.compile("__cr.init\((.*?)\)</script>", re.S)
            # 这里使用demjson库
            script = demjson.decode(re.findall(pattern, response.text)[0])
            print(script)
            chapter_addr = script["chapter_addr"]
            chapter_id = script["chapter_id"]
            chapter_name = script["chapter_name"]
            end_var = script["end_var"]
            comic_name = script["comic_name"]
            # 解析imgpath~图片的加密方式
            imgpath = get_img_path(chapter_addr, chapter_id)
            # 保存的目标文件路径
            path = "{}/{}/".format(comic_name, chapter_name)
            # 判断文件目录是否存在，不存在则新建
            if not os.path.exists(path):
                os.makedirs(path)

            for page in tqdm(range(1, end_var + 1)):
                with open(path + "{}.webp".format(page), 'wb') as f:
                    # 每一张图片的url
                    img_url = "https://mhpic.xiaomingtaiji.net/comic/{}{}.jpg-zymk.middle.webp".format(imgpath, page)
                    res = requests.get(url=img_url, headers=headers, timeout=5)
                    if res.status_code == 200:
                        f.write(res.content)
                # 随机休眠一会，不要爬太快
                time.sleep(random.random())

    except Exception as e:
        print(e)


def get_img_path(chapter_addr, chapter_id):
    """
    读取js逆向源代码，如果多次调用，一直打开，读取后又关闭文件，十分占据计算机内存
    with open("./getSrc.js","r",encoding="utf-8") as f:
        resource = f.read()
    :param :resource js源文件
    :return:
    """
    resource = '''
    function getSrc(chapter_addr, chapter_id) {
        return chapter_addr.replace(/./g, function (a) {
            return String.fromCharCode(a.charCodeAt(0) - chapter_id % 10)
        })
    }
    '''
    # 编译js源码
    x = execjs.compile(resource)
    result = x.call("getSrc", chapter_addr, chapter_id)
    print(parse.unquote(result))
    return result


def download_images():
    comic_list, numbers = get_comic()
    print("已更新到 {} ,总集数：{}".format(comic_list[-1]["title"], numbers))
    number1 = int(input("请输入你的下载起始集数（小于总集数）："))
    number2 = int(input("请输入你的下载截止集数（小于总集数）："))
    if number1 <= number2:
        for i in range(number1, number2 + 1):
            print("\033[5;37;40m正在下载第{}章漫画~~~\033[0m".format(i + 1))
            # 获取章节url
            url = comic_list[i]["url"]
            get_images(url)
            time.sleep(random.randint(1, 4))
    else:
        print("下载起始集数应该小于截止集数")


if __name__ == '__main__':
    # get_comic_list()
    download_images()
