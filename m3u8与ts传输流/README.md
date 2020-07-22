### m3u8基本概念

什么是m3u8文件? M3U8文件是指UTF-8编码格式的M3U文件。

**M3U文件是记录了一个索引纯文本文件，打开它时播放软件并不是播放它，而是根据它的索引找到对应的音视频文件的网络地址进行在线播放**。

原视频数据分割为很多个TS流，每个TS流的地址记录在m3u8文件列表中。

m3u8是苹果公司推出一种视频播放标准，是m3u的一种，不过 编码方式是utf-8，是一种文件检索格式，将视频切割成一小段一小段的ts格式的视频文件，然后存在服务器中（现在为了减少I/o访问次数，一般存在服务器的内存中），通过m3u8解析出来路径，然后去请求。

### m3u8文件样式

m3u8是一个索引纯文本文件，下面展示m3u8部分内容，其中以.ts结尾的url才是正在的被切片的视频文件链接

```text
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:10
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-KEY:METHOD=AES-128,URI="key.key"
#EXTINF:10.000000,
mYexOkq6386000.ts
#EXTINF:10.000000,
mYexOkq6386001.ts
。。。
```

上面就是一个 m3u8 文件的前一部分，**我们爬虫需要关注的是加密方式是 AES-128** 。然后去把 index.m3u8 替换成 key.key，即可获取到加密的密钥，这个密钥 key 将会是我们后续解码文件的关键，没了它下载得到的文件是没有意义的。


### 嵌套的m3u8文件

我们获取m3u8的真实url时，有可能会遇到嵌套的m3u8。比如从某个地址（https://abc.net/xx/xx/.m3u8) 下载地址是 (https://abc.net/xx/xx/index.m3u8）捕获的index.m3u8文件内容如下

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1000000,RESOLUTION=720x480
1000kb/hls/index.m3u8
```
这是一个嵌套的m3u8，对我们有帮助的m3u8可以通过地址https://abc.net/xx/xx/1000kb/hls/index.m3u8 下载,查看其索引纯文本文件

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:2
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-KEY:METHOD=AES-128,URI="key.key"
#EXTINF:1.668333,
6qYsze1019000.ts
#EXTINF:0.834167,
6qYsze1019001.ts
#EXTINF:0.834167,
6qYsze1019002.ts
……
下面还有很多
……
```

如果没有#EXT-X-KEY这一行，就是没有加密，METHOD表明了加密方式，URI是密匙文件的地址，有的网站会直接写出详细地址，有些则不会，甚至有些会对uri地址进行加密，对uri地址解密的方法百度上有很多

密匙文件一般为16字节，在浏览器中输入URI可能不会直接下载密匙，而是在浏览器中显示密匙

我的密匙文件内容是

`5fa1f545ebbba8bd`

这里没有给出详细地址，一般来说就是默认为相对路径，因此实际URI为https://abc.net/xx/xx/1000kb/hls/key.key

6qYsze1019xxx.ts是视频流文件的获取地址，实际地址是https://abc.net/xx/xx/1000kb/hls/6qYsze1019xxx.ts

可以通过猫抓这些浏览器视频捕获插件获得这些URI地址，将视频定位到末尾，猫抓的信息更新后会显示最后一个视频流的文件（就是6qYsze1019xxx.ts这些文件里面xxx数字最大的那个），然后可以通过迅雷等软件下载这些视频流

 

下载后的视频流如果被加密了，是无法直接播放的。通过上面获取的index.m3u8（获取地址是https://abc.net/xx/xx/1000kb/hls/index.m3u8，不是https://abc.net/xx/xx/index.m3u8，下同）和key.key的配合，可以通过使用ffmpeg等软件进行解密并且合并，使用格式工厂也可以合并，但是每次输入文件最大是50个，不方便，有了index.m3u8和视频流，使用ffmpeg可以直接使用一行命令来合并所有视频流文件


### 解密过程

1. 下载index.m3u8、key.key、视频流

2. 首先安装ffmpeg，并且设置好环境变量

3. 将index.m3u8、key.key放入视频流所在的目录，将key.key改名为key.m3u8（因为key不是ffmpeg内置格式，使用key.key会报错）

4. 在命令行中，进入视频流所在目录，输入以下命令即可完成解密以及合并的工作，最后会在当前目录下生成完整的输出视频out.mp4

`ffmpeg -i index.m3u8 out.mp4`

> 解密方式二


当然了，最简单的办法当然是直接从网上获取视频，免去下载视频流的步骤，命令如下

-i后面指定m3u8文件的URI

out.mp4是生成文件名，默认是命令行的当前目录，可以通过绝对路径指定具体位置，如G:\abc\xxx.mp4

`ffmpeg -i https://abc.net/xx/xx/1000kb/hls/index.m3u8 out.mp4`


### 合并.ts结尾的传输流
> ts文件已经下载至本地

假设已经将下载好了的ts，key文件都保存在同一目录下，此时我们就需要修改源m3u8文件了，修改m3u8文件中key的uri路径和ts文件的路径为本地路径。

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-TARGETDURATION:13
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-KEY:METHOD=AES-128,URI="e:/20180125/key.key"
#EXTINF:12.5,
e:/20180125/GBDYO3576000.ts
#EXTINF:12.5,
e:/20180125/GBDYO3576001.ts
#EXTINF:12.5,
e:/20180125/GBDYO3576002.ts
```

### DPlayer视频播放

+ [DPlayer官网](http://dplayer.js.org/guide.html)
+ [弹幕池搭建](https://www.moerats.com/archives/838/)
