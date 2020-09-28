网页url：http://www.pufei8.com/

### 1.加密原理

在每一章节，按住 `Ctrl+U` 查看网页源代码，其中的一个\<script\>包裹的就是加密源代码

```javascript
function base64decode(str){var base64EncodeChars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";var base64DecodeChars=new Array(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,62,-1,-1,-1,63,52,53,54,55,56,57,58,59,60,61,-1,-1,-1,-1,-1,-1,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,-1,-1,-1,-1,-1,-1,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,-1,-1,-1,-1,-1);var c1,c2,c3,c4;var i,len,out;len=str.length;i=0;out="";while(i<len){do{c1=base64DecodeChars[str.charCodeAt(i++)&255]}while(i<len&&c1==-1);if(c1==-1){break}do{c2=base64DecodeChars[str.charCodeAt(i++)&255]}while(i<len&&c2==-1);if(c2==-1){break}out+=String.fromCharCode((c1<<2)|((c2&48)>>4));do{c3=str.charCodeAt(i++)&255;if(c3==61){return out}c3=base64DecodeChars[c3]}while(i<len&&c3==-1);if(c3==-1){break}out+=String.fromCharCode(((c2&15)<<4)|((c3&60)>>2));do{c4=str.charCodeAt(i++)&255;if(c4==61){return out}c4=base64DecodeChars[c4]}while(i<len&&c4==-1);if(c4==-1){break}out+=String.fromCharCode(((c3&3)<<6)|c4)}return out};
var ret_classurl = '/mh/8/';
var comicname = "食色大陆";
var viewid = "381759";
var viewtype = "1";
var viewname = "398、肥宅快乐水";
var photosr = new Array();
packed="ZXZhbChmdW5jdGlvbihwLGEsYyxrLGUsZCl7ZT1mdW5jdGlvbihjKXtyZXR1cm4gYy50b1N0cmluZygzNil9O2lmKCEnJy5yZXBsYWNlKC9eLyxTdHJpbmcpKXt3aGlsZShjLS0pe2RbYy50b1N0cmluZyhhKV09a1tjXXx8Yy50b1N0cmluZyhhKX1rPVtmdW5jdGlvbihlKXtyZXR1cm4gZFtlXX1dO2U9ZnVuY3Rpb24oKXtyZXR1cm4nXFx3Kyd9O2M9MX07d2hpbGUoYy0tKXtpZihrW2NdKXtwPXAucmVwbGFjZShuZXcgUmVnRXhwKCdcXGInK2UoYykrJ1xcYicsJ2cnKSxrW2NdKX19cmV0dXJuIHB9KCdjWzFdPSJiL2UvYS9kL2YvaS5nLzAiO2NbMl09ImIvZS9hL2QvZi9rLmcvMCI7Y1szXT0iYi9lL2EvZC9mL3QuZy8wIjtjWzRdPSJiL2UvYS9kL2Yvbi5nLzAiO2NbNV09ImIvZS9hL2QvZi9sLmcvMCI7Y1s2XT0iYi9lL2EvZC9mL2ouZy8wIjtjWzddPSJiL2UvYS9kL2YvaC5nLzAiO2NbOF09ImIvZS9hL2QvZi9tLmcvMCI7Y1s5XT0iYi9lL2EvZC9mL3UuZy8wIjtjW3ZdPSJiL2UvYS9kL2Yvby5nLzAiO2NbcF09ImIvZS9hL2QvZi9xLmcvMCI7Y1tyXT0iYi9lL2EvZC9mL3MuZy8wIjsnLDMyLDMyLCd8fHx8fHx8fHx8MDd8aW1hZ2VzfHBob3Rvc3J8MjF8MjAyMHwwMXxwbmd8NDdmMDMyMTcxNXw0NzFiYTUwNWYzfDQ3MDk4ZGRjZWF8NDdlMmNiMzg5Znw0NzQ0MDAxNjhkfDQ3MWNmY2IzZmN8NDdhMmY1YTQyYnw0N2ZlNDc5OTQxfDExfDQ3ZjVlMzJiZTl8MTJ8NDcxMWJkNmY0Mnw0N2IzMjgxMjgyfDQ3NTlkYmYzNTd8MTAnLnNwbGl0KCd8JyksMCx7fSkpCg==";
eval(eval(base64decode(packed).slice(4)));  // 核心加密原理
var maxpages=photosr.length-1;
var dm456 = {vid:'8',pid:'381759',en:'',vt:'食色大陆',pt:'398、肥宅快乐水'};
```

### 2.Eval原理

☆☆☆ [Eval函数知识总结](https://www.cnblogs.com/syp1/p/5436304.html)

> eval是什么？（解析器）

eval是一个函数，看本质function  eval() { [native code] }。
但是其实是一个解析器，表示执行eval括号里的东西，**它可以直接在浏览器上的console调试台上直接运行**。

### 3.后台传递二进制文件

eval解密后的参数为
```js
let photosr = [];
// eval(base64decode(packed).slice(4))
photosr[1]="images/2020/07/21/01/471ba505f3.png/0";
photosr[2]="images/2020/07/21/01/47e2cb389f.png/0";
photosr[3]="images/2020/07/21/01/47b3281282.png/0";
photosr[4]="images/2020/07/21/01/47a2f5a42b.png/0";
photosr[5]="images/2020/07/21/01/474400168d.png/0";
photosr[6]="images/2020/07/21/01/47098ddcea.png/0";
photosr[7]="images/2020/07/21/01/47f0321715.png/0";
photosr[8]="images/2020/07/21/01/471cfcb3fc.png/0";
photosr[9]="images/2020/07/21/01/4759dbf357.png/0";
photosr[10]="images/2020/07/21/01/47fe479941.png/0";
photosr[11]="images/2020/07/21/01/47f5e32be9.png/0";
photosr[12]="images/2020/07/21/01/4711bd6f42.png/0";

// rows为图片集
rows = photosr.slice(1);

```

图片完整的url：http://res.img.fffmanhua.com/images/2020/07/21/01/47e2cb389f.png/0

**复制完整的url后，复制粘贴到浏览器访问时，不是显示图片，而是直接下载一个没有后缀名的文件，以图片的形式打开，居然可以显示图片内容了，将文件后缀名修改为 *.png* ,此刻图片完整展示出来，料定应该是后端传递给前端是将图片转换为二进制文件的文件流**

二进制文件访问：音视频，图片
```python
# -*- coding:utf-8 -*-
import requests

url = "http://res.img.fffmanhua.com/images/2020/07/21/01/47e2cb389f.png/0"
response = requests.get(url, stream=True)
with open("./1.png", 'wb') as f:
    f.write(response.content)
```

### 4.状态码304 Not Modified

当我们爬取某些网站时[扑飞漫画](http://www.pufei8.com/)中会遇到对浏览器缓存下请求资源返回304的情况流量的计费的情况，这里就需要了解HTTP 304的响应状态的资源更新机制。

这是因为该网站采取了强缓存验证， 服务器将要爬取的内容在本地做了缓存，再次请求的时候，会首先检查本地缓存中是否已存在，如果有就返回304

首先看一个关于304请求的响应头的信息，这里面有两个比较重要的请求头字段：`If-Modified-Since` 和 `If-None-Match`，这两个字段表示发送的是一个条件请求。

![](http://7xkn2v.dl1.z0.glb.clouddn.com/QQ20160215-0.png)

当客户端缓存了目标资源但不确定该缓存资源是否是最新版本的时候, 就会发送一个条件请求，这样就可以辨别出一个请求是否是条件请求，在进行条件请求时,客户端会提供给服务器一个If-Modified-Since请求头,其值为服务器上次返回的Last-Modified响应头中的Date日期值,还会提供一个If-None-Match请求头,值为服务器上次返回的ETag响应头的值。

服务器会读取到这两个请求头中的值,判断出客户端缓存的资源是否是最新的,如果是的话,服务器就会返回HTTP/304 Not Modified响应头, 但没有响应体.客户端收到304响应后,就会从本地缓存中读取对应的资源.

**解决方案：**
- 方案一：请求头里的 ***If-Modified-Since、If-None-Match和Cache-control***，都必须禁用
- 方案二：请求头里User-Agent为动态的

```python
headers = {
    "Host": "www.pufei8.com",
    "Referer": "http://www.pufei8.com/",
    'Accept': 'text/html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3945.88 Safari/537.36"
}
```