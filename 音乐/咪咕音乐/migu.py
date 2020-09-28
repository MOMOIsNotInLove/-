# -*- coding:utf-8 -*-
import random
import re
import time
import requests

headers = {
    'Referer': 'https://m.music.migu.cn/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Mobile Safari/537.36'
}
detail_url = 'http://m.music.migu.cn/migu/remoting/cms_detail_tag?cpid={copyrightId}'
player_url = 'https://app.pd.nf.migu.cn/MIGUM3.0/v1.0/content/sub/listenSong.do?channel=mx&copyrightId={copyrightId}&contentId={contentId}&toneFlag={toneFlag}&resourceType={resourceType}&netType=00'


def get_url(url: str):
    """
    http://music.migu.cn/v3/music/song/*********
    author、audioName、audios
    """
    data = {}
    # get copyrightId
    copyrightId = re.findall(r"song/(\d+)", url)[0]

    # get detail
    rep = requests.get(detail_url.format(copyrightId=copyrightId), headers=headers, timeout=6)
    if rep.status_code != 200 or rep.json()["data"] is None:
        print({"msg": "获取失败,请检查链接是否正确"})
        return None

    json = rep.json()["data"]  # type: dict

    # author
    singerName = json["singerName"]  # type: list
    # 解决作者名为空1的bug
    author = "null" if len(singerName) < 1 else "&".join(singerName)

    # audioName
    audioName = json["songName"]
    # contentId
    c_item = json.get("qq")  # type:dict

    if not c_item:
        return {"msg": "获取失败"}
    contentId = c_item["productId"]

    # toneFlag
    toneFlag = "HQ" if json["hasHQqq"] == "1" else "LQ"

    video_url = player_url.format(copyrightId=copyrightId,
                                  contentId=contentId,
                                  toneFlag=toneFlag,
                                  resourceType=2)

    data["author"] = author
    data["audioName"] = audioName
    data["videos"] = video_url
    data["coverL"] = json["picL"]
    data["coverM"] = json["picM"]
    data["coverS"] = json["picS"]

    return data


def search(kw, page):
    search_url = "https://m.music.migu.cn/migu/remoting/scr_search_tag?rows=10&type=2&keyword={}&pgc={}".format(kw,page)
    session = requests.Session()
    try:
        response = session.get(url=search_url, headers=headers, timeout=10)
        if response.status_code == 200:
            rows = response.json()
            # 数据总数
            counts = rows.get("pgt")
            #
            musics = rows["musics"]
            numbers = []
            for i in musics:
                cp = "http://music.migu.cn/v3/music/song/" + i["copyrightId"]
                data = get_url(cp)
                if data is None:
                    continue
                numbers.append(data)
                time.sleep(random.random())
            return {"count": counts, "page": page, "rows": numbers}
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # url = "http://music.migu.cn/v3/music/song/60054702021"
    # url = "http://music.migu.cn/v3/music/song/60054702021"
    # print(get_url(url))
    print(search("不能说的秘密", "1"))
