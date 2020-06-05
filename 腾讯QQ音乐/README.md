## 腾讯QQ音乐

### 1.参考文章

+ [QQ音乐爬虫之放弃的路](https://blog.csdn.net/jiangerchi/article/details/105618528) :完全贴合我此时心情
+ [QQ音乐爬虫](https://blog.csdn.net/weixin_44119390/article/details/90812246)

### 2. 您播放的歌曲仅限客户端播放，建议您打开客户端进行播放

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