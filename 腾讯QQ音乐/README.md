## 腾讯QQ音乐

### 1.参考文章

+ [QQ音乐爬虫之放弃的路](https://blog.csdn.net/jiangerchi/article/details/105618528) :完全贴合我此时心情
+ [QQ音乐爬虫](https://blog.csdn.net/weixin_44119390/article/details/90812246)

### 2. 您播放的歌曲仅限客户端播放，建议您打开客户端进行播放

**PC网页版**

腾讯QQ音乐爬取练习

> 专辑url相关

- 专辑列表url：https://c.y.qq.com/soso/fcgi-bin/client_search_cp?t=8&p=1&n=10&w=周杰伦&format=json


> 单曲url相关

原来的url很长，经过删选一些无用的请求参数，缩减为：
- 搜索url： https://c.y.qq.com/soso/fcgi-bin/client_search_cp?new_json=1&cr=1&catZhida=1&p=1&n=10&w=一路向北&format=json&inCharset=utf8
- 评论url： https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?biztype=1&topid=106291297&cmd=8&pagenum=0&pagesize=25
- 歌曲下载url1： http://180.153.119.143/amobile.music.tc.qq.com/C400{获取的播放列表的mid}.m4a?guid={guid，固定值}&vkey={另一个url返回的vkey值}&uin=4689&fromtag=66
- 歌曲下载url2： http://isure.stream.qqmusic.qq.com/C400{获取的播放列表的mid}.m4a?guid={guid，固定值}&vkey={另一个url返回的vkey值}&uin=4689&fromtag=66
- 获取vkey的url（即下面展示的新旧两个api）


解析加密参数:通过博客（https://blog.csdn.net/weixin_44119390/article/details/90812246）发现，

到目前2020-06-04为止，其实现在的QQ音乐网站已经相比于文章描述的时候已经改版。
+ 现在有两个API接口：
   1. 文章所提及的API（https://u.y.qq.com/cgi-bin/musicu.fcg）接口，请求方式为【GET】,请求参数也只有data部分【至今可用】
   2. 新版的API已经变为（https://u.y.qq.com/cgi-bin/musics.fcg），请求方式为【GET】,请求参数必须包含sign和data部分

+ 参数说明：
   + guid：唯一值，与每一个账户相绑定
   + mid = 每一首歌曲的唯一标识id
   + uin = 唯一值，应该为账户名

+ 腾讯QQ音乐爬虫的流程示意：
   1. 先通过搜索API或其它方式获取每一首歌曲的mid（形如 004GNa6e1ze5dk）
   2. 通过新旧API获取vkey，为了拼接成最后的音频url
   3. 遍历下载歌曲 
<hr>

有些歌曲会弹出“您播放的歌曲仅限客户端播放，建议您打开客户端进行播放”，那我们该怎么处理呢？
<fancybox>![](https://cdn.jsdelivr.net/gh/FioraLove/Images/qq_music.png)</fancybox>

**模拟移动端访问**

1. 谷歌浏览器，F12。调试成移动端，网址已成移动端的了。

2. 提取歌曲播放url，经过一番抓包，发现了其url

播放url：https://i.y.qq.com/v8/playsong.html?songmid=001OyHbk2MSIi4
songmid为每一首歌曲的唯一标识id

3. 发现网页源代码里的\<script>标签里包含了完整的歌曲播放路径

```text
http://aqqmusic.tc.qq.com/amobile.music.tc.qq.com/C400000S7TGL43hhBO.m4a?
guid=7238047136
&vkey=7B4D077C97CA0AC467D1B79158CEE05B0572A383CD4CA5753FCCDA09A2887C27A574702780A8C089C21C17FE0968099C984F6BBAAA591F3A
&uin=4689&
fromtag=38
```