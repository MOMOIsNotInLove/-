# Net-Spider

**不积跬步，无以至千里；不积小流，无以成江海**

新手小白们（[Galonewxr](https://github.com/Galonewxr)，张先生，胡某）~~持续更新中〜随意Fork，Star，大佬萌多多issue哦。目前更新: 



<p align="center">
    <a href="https://AhriLove.top"><img src="https://img.shields.io/badge/AhriLove-%E4%B8%AA%E4%BA%BA%E7%BD%91%E7%AB%99-orange"></a>
    <a href="https://github.com/python/cpython"><img src="https://img.shields.io/badge/Python-3.7-FF1493.svg"></a>
    <a href="https://opensource.org/licenses/mit-license.php"><img src="https://badges.frapsoft.com/os/mit/mit.svg"></a>
    <a href="https://github.com/FioraLove/Net-Spider"><img src="https://img.shields.io/github/repo-size/FioraLove/Net-Spider"></a>
    <a href="https://github.com/FioraLove/Net-Spider/graphs/contributors"><img src="https://img.shields.io/badge/contributors-2-blue"></a>
    <a href="https://github.com/shengqiangzhang/examples-of-web-crawlers/stargazers"><img src="https://img.shields.io/github/stars/FioraLove/Net-Spider.svg?logo=github"></a>
    <a href="https://github.com/FioraLove/Net-Spider/network/members"><img src="https://img.shields.io/github/forks/FioraLove/Net-Spider.svg?color=blue&logo=github"></a>
    <a href="https://www.python.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" align="right" height="48" width="48" ></a>
</p>
<br />


| 项目 | 状态|  |项目 | 状态|
|  ----  | ----  | ----  | ---- |----|
| 抖音视频无水印解析🎶🎶🎶 | 🛠🛠🛠 |  | [bilibili音视频解析和弹幕获取🐱‍👓](https://bilibili.com) | ✅✅✅|
| 知音漫客图片加密 🔥 | ✅✅✅ |  |世纪佳缘信息👨‍👩‍👧‍👦  |✅✅✅| 
| 小鸡词典🐥🐥 | ✅✅✅ |  |拉钩网职位信息✔  |✅✅✅| 
| 斗鱼主播列表🐟🐟🐟 | ✅✅✅ |  |openlaw裁决网🕵🕵🕵  |✅✅✅| 
| CSDN文章 🌍🌎🌏 | ✅✅✅ |  |代理池🚣‍♂️🚣‍♂️🚣‍♂️  |✅✅✅| 
| 马蜂窝🐝🐝🐝 | ✅✅✅ |  |京东评论💋💋💋  |✅✅✅| 
| 淘宝登录 | 🛠🛠🛠 |  |[漫画台](https://www.manhuatai.com/)  |✅✅✅| 
| [腾讯QQ音乐](https://y.qq.com/)🎹🎹🎹 | 🛠🛠🛠 |  | 《我的轻小说爬取程序不可能这么可爱》📚📚📚  |✅✅✅| 
| [今日头条](https://www.toutiao.com/)📺📺📺 | 🛠🛠🛠|  | [Eval加密的扑飞漫画](http://www.pufei8.com/) 📕📕📕| ✅✅✅|





<br>
<hr>

> 近期任务安排:

- [x] 整理Markdown手册
- [ ] 改善项目
   - [ ] 知音漫客设置下载起始与截止集数
   - [x] 今日头条的`关注`和`粉丝`解析逆向出各个参数了，请求后，一直返回空白
   - [ ] 修复抖音_signaturn的加密js中“webdriver”未定义
- [ ] 待完成项目
   - [ ] 腾讯QQ音乐提示“**您播放的歌曲仅限客户端播放**”时，以移动端方式访问(其实很简单的，但要全面重构代码，均通过网页源代码的\<script>标签里包含了完整的歌曲播放路径)
   - [x] 西瓜视频解析

<br>
<hr>

## API接口汇集板块

1. 微博热搜：

```text
https://s.weibo.com/top/summary/summary?cate=realtimehot
```

2. 淘宝商品详情

不要使用decodeURIComponent url解码函数，会出错

```text
https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?jsv=2.4.8&appKey=12574478&t=1591867003132&sign=fd63bc888213522424d93c302c9ef5bd&api=mtop.taobao.detail.getdetail&v=6.0&dataType=jsonp&ttid=2017%40taobao_h5_6.6.0&AntiCreep=true&type=jsonp&callback=mtopjsonp2&data=%7B%22itemNumId%22%3A%22567263006792%22%7D
```

3. GNE新闻提取器，是抽取器的一种，而不是爬虫

官方文档：https://github.com/kingname/GeneralNewsExtractor
GNE在线测试：http://122.51.39.219/
通过抓包分析，找出了GNE在线测试的API接口，只需要调用这个接口，就可以或去新闻页内容。**比如今日头条项目，爬取下来的新闻url，就可以通过GNE就可以提取其标题、时间、作者、新闻内容和图片**

+ URL: http://122.51.39.219/extract
+ 请求方法：POST
+ 请求参数：*除html参数外，其它都是非必须参数*

```python

{
   "html":"目标网页源代码",
   "title_xpath":"用户自定义的提取网页的标题的xpath",
   "author_xpath":"用户自定义的提取网页的作者的xpath",
   "publish_time_xpath":"用户自定义的提取网页的发行时间的xpath",
   "host":"主机",
   "with_body_html":false,
   "noise_node_list":[]
}
```

+ 响应内容：json数据格式

```json
{
   "title": "为了出cos，骚男的胸部是越来越大了",
   "author": "",
   "publish_time": "",
   "content": "",
   "images": []
}
```




