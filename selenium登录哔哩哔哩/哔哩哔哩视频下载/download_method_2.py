# -*- coding:utf-8 -*-
import re


from tqdm import tqdm
import json
import requests
from threading import Thread
# 禁用安全请求警告
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)





"""
Bilibili视频下载小程序
亲测有效！！！
思考：
1. 先可以利用：https://search.bilibili.com/all?keyword=搜索内容&page=页码，获取查询结果集（
    1.1 可以选择在源代码里获取bv号，因此可以使用re，xpath，pyquery提取所有的bv号
    1.2 可以在api接口中，利用json获取bv号）
2. 遍历每一个bv号，多线程分别下载音频和视频
3. b站请求头的range要特别注意，表示的音视频文件大小（b站是将音视频分别做切片处理，切成好多段，当我们
    请求某一个音视频的url，并将range尽可能设置最大，就可以通过某一个切片的url获取整个音视频文件）

4. 关于清视频晰度：

      方法	            描述
    未登录状态	抓取的视音频url参数：mid=0
    登录状态	    抓取的视音频url参数：mid=xxx(一串数字)


"""

session = requests.session()


class BilibiliSpider:
    def __init__(self, url):
        self.url = url
        self.pageHeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
        }
        self.dataHeaders = {
            'accept': '*/*',
            'accept-encoding': 'identity',
            'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,zh-HK;q=0.5',
            'origin': 'https://www.bilibili.com',
            'range': 'bytes=0-169123900000000',
            'referer': 'https://www.bilibili.com/video/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        }

    def get_url(self):
        """
        请求视频播放页面，在源码中获取视音频链接和视频名称
        :return: 视频链接、音频链接、视频名称
        """
        htmlData = requests.get(self.url, headers=self.pageHeaders, verify=False).text
        urlData = json.loads(re.findall('<script>window.__playinfo__=(.*?)</script>', htmlData, re.M)[0])
        videoUrl = urlData['data']['dash']['video'][0]['baseUrl']
        audioUrl = urlData['data']['dash']['audio'][0]['baseUrl']
        name = re.findall('<h1 title="(.*?)" class="video-title">', htmlData, re.M)[0]
        return videoUrl, audioUrl, name

    def download_video(self, videoUrl, name):
        """
        传入url和名称，开始下载
        :param videoUrl:    视频链接
        :param name:        视频名称
        :return:
        """
        chunk_size = 1024
        size = 0
        response = session.get(videoUrl, headers=self.dataHeaders, stream=True)
        content_size = int(re.findall(r"/(.*)", response.headers['Content-Range'], re.S)[0])
        videoContent = response.content
        print('Start download,[File size]:{size:.2f} MB'.format(size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
        with open('%s.mp4' % name, 'wb') as f:
            for data in tqdm(response.iter_content(chunk_size=1024)):
                f.write(data)
            f.flush()
            print('video download Success')

    def download_audio(self, audioUrl, name):
        """
        传入url和名称，开始下载
        :param audioUrl:    音频链接
        :param name:        音频名称
        :return:
        """
        audioContent = session.get(audioUrl, headers=self.dataHeaders).content
        with open('%s.mp3' % name, 'wb') as f:
            f.write(audioContent)
            f.close()
            print('audio download Success')

    def main(self):
        """
        主程序，利用多线程下载视音频会比较快
        :return:
        """
        videoUrl, audioUrl, name = self.get_url()
        videoThread = Thread(target=self.download_video, args=(videoUrl, name,))
        audioThread = Thread(target=self.download_audio, args=(audioUrl, name,))
        videoThread.start()
        audioThread.start()
        videoThread.join()
        audioThread.join()
        # 退出保持会话
        session.close()


if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/BV1n7411r7r3'
    spider = BilibiliSpider(url)
    spider.main()
