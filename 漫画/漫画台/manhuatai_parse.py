# -*- coding:utf-8 -*-
import random
import time
import requests
import re
import json
from pyquery import PyQuery as pq


def get_manhua():
    comic_url = "https://www.manhuatai.com/nitianxieshen/"
    comic_uid = str(input("请输入漫画的表示id: e.g.,15194"))
    headers = {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
    }
    session = requests.Session()

    response = session.get(url=comic_url, headers=headers, timeout=10)
    if response.status_code == 200:
        doc = pq(response.text)
        rows = doc(".chapter-list li")
        for i in rows.items():
            chapter_number = int(i.attr("data-id"))+1
            cid = i.attr("data-chapter")
            title = i("a").attr("title")
            link = "https://www.manhuatai.com"+i("a").attr("href")
            print("=============== 正在打印 漫画章节ID：{} ===================\n".format(cid))
            try:
                time.sleep(random.randint(1, 2))
                results = session.get(url=link, headers=headers, timeout=10)
                if results.status_code == 200:
                    pattern = re.compile("current_chapter:.*?(.*?)\}",  re.S)
                    current_chapter = re.findall(pattern, results.text)[0]
                    # title = re.findall('chapter_name:"(.*?)",',current_chapter,re.S)[0]
                    start_page = re.findall('start_num:(.*?),',current_chapter, re.S)[0]
                    # chapter_id = re.findall('chapter_id:(.*?),',current_chapter, re.S)[0]
                    end_page = re.findall('end_num:(.*?),',current_chapter, re.S)[0]
                    rule = re.findall('rule:"(.*?)"', current_chapter, re.S)[0]
                    array =[]
                    for j in range(int(start_page),int(end_page)+1):
                        # https://mhpic.dm300.com/comic/X/仙帝归来/第25话F1_210122/5.jpg-mht.middle.webp
                        img_url = "https://mhpic.dm300.com"+rule.split("$$")[0]+str(j)+".jpg-mht.middle.webp"
                        array.append(img_url)
                    images_list = json.dumps(array, ensure_ascii=False)
                    time.sleep(random.randint(1, 2))
                    base_url = "http://127.0.0.1:8001/nmsl/api/comic/chapter/"
                    data = {
                        "uid": comic_uid,
                        "cid": str(cid),
                        "chapter_title": title,
                        "chapter_number": int(chapter_number),
                        "images_url": images_list
                    }
                    result = requests.post(url=base_url, headers=headers, data=data, timeout=20)
                    if result.status_code != 200:
                        continue

            except Exception as e:
                print(e)
                continue


if __name__ == '__main__':
    get_manhua()
