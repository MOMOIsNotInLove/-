>知音漫客

### 知音漫客的加密方式：

一，首先漫画的搜索，漫画每章节的标题，每章节的图片数量，这些东西都是最基础的数据，直接使用get方法就可以得到。
二，对于付费章节来说，每张图片的src链接都是使用js加密的。熟悉js的应该可以很简单就解析出来（本人完全小白，花费了很长时间解析，主要是走了很多弯路）。以下就是js解析的过程。
————————————————
版权声明：本文为CSDN博主「那年葬下的梦」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：**https://blog.csdn.net/u011283565/article/details/99301812**


知音漫客的三个关键API：

- 漫画列表大全以及编号： https://www.zymk.cn/nodeapi/comic/allComic/ 【GET】
- 具体某部漫画：https://www.zymk.cn/漫画的编号/ 这里传入的漫画的编号，不是漫画名，具体的编码由请求第一个api，返回后的编码值【GET】 
- ★★★漫画的某个章节：https://www.zymk.cn/漫画名编号/章节编号.html


**破解漫画的关键就在于下面这段网页源代码中的script里面**
```html
<div class="comiclist">
    <script>
        let cnzz_comic = ["_trackEvent", "妖神记", "zymk_pc", "", 857];
        let _czc = [["_letAccount", "1261814609"]];
        _czc.push(cnzz_comic);
        __cr.init({
            chapter_addr: "a-:N-M=-I>-A>-M?-I=-AM-M@-IM-J8-:N9-M@-IN-AL-:N",
            start_var: 1,
            end_var: 14,// 最大页数
            comic_id: 857,
            comic_name: "妖神记",
            chapter_id: 14088,
            chapter_name: "1话",
            previd: "",
            prevname: "",
            nextid: "14155",
            nextname: "2话",
            readmode: 1,
            readtype: 0,
            maxpreload: 5,
            defaultminline: 1,
            domain: "zymkcdn.com",
            comic_definition: {
                high: "-zymk.high",
                low: "-zymk.low",
                middle: "-zymk.middle"
            },
            price: 0,
            webview: ""
        })
    </script>
</div>
```

### 图片的src加密

**每张图片的src都是经过加密的，核心加密的方式如下**

```js
e.prototype.getPicUrl = function(e) {
    var t = this.comic_size || ""
      , i = this.linedata[this.chapter_id].use_line
      , a = e + this.start_var - 1 + this.image_type + t;
    return "//" + i + "/comic/" + this.imgpath + a
}
```

+ e = 表示页数
+ t = ""-zymk.middle.webp""
+ i = "mhpic.xiaomingtaiji.net" 或者"mhpic.xiaomingtaiji.cc" 这两个都是知音漫客的阿里域名
+ a = "页数.jpg-zymk.middle.webp"



解析后的目标url：**https://mhpic.xiaomingtaiji.net/comic/Y/妖神记/1话/5.jpg-zymk.middle.webp**

接下来就是解析imgpath：


```js
e.prototype.init = function(e) {
    if (!e)
        return !1;
    this.setInitData(e),
    this.charcode(this.decode),
    t("base").attr("target", "_self"),
    this.getLine()[this.chapter_id].expire < (new Date).getTime() && t.ajax({
        url: "//server." + this.domain + "/mhpic.asp?callback=" + x + ".setLine",
        dataType: "script",
        scriptCharset: "utf-8"
    });
    4 !== this.readmode ? (this.showPic(),
    1 === this.readmode && this.initpage(".footpage")) : this.initDoubleMode()
}
```

经过断点调试发现这个 **this.charcode(this.decode)** 便是加密的核心,它就是**imgpath**
先全局搜索this.decode，发现这是一个常量，已经定义好了

```js
decode = "``ds/jnhqbui>``ds/jnhqbui/sfqmbdf)0/0h-gvodujpo)b*|sfuvso!Tusjoh/gspnDibsDpef)b/dibsDpefBu)1*.``ds/dibqufs`je&21*~*";
```

继续全局搜索`charcode()`函数，展示：
```js
function charcode(decode) {
    decode.replace(/./g, function(e) {return String.fromCharCode(e.charCodeAt(0) - 1)})
}
```

charcode函数里代入decode参数，运行结果为：

返回结果仔细看其实是一个函数，只是将其字符串化了，**cr.imgpath**便是图片的imgpath（**chapter_addr就是我们源码中已有数据。在js中||代表逻辑或，也就是说只要chapter_addr非空，imgpath就等于它**）
```js
"cr.imgpath=cr.imgpath.replace(/./g,function(a){return String.fromCharCode(a.charCodeAt(0)-__cr.chapter_id%10)})"
```

👇js定位（**这是最核心的代码**）

```javascript
function getSrc(chapter_addr, chapter_id) {
    return chapter_addr.replace(/./g, function (a) {
        return String.fromCharCode(a.charCodeAt(0) - chapter_id % 10)
    })
}
```

execjs运行getSrc函数后的返回结果：
```text
Y%2F%E5%A6%96%E7%A5%9E%E8%AE%B0%2F1%E8%AF%9D%2F
~~ 

```
以前还年轻的时候，总喜欢康康 ”知音漫客“。读书住校时，谁有一本漫画书都会在寝室里传来传去，都抢着看，十分开心。
最近听说 龙族Ⅴ 又断更了🔪🔪🔪，想看时居然要会员了。。。私下发现每一张图片都是js加密的，耗费了一把头发终于找到了加密原理，发现其实不管是不是会员都可以浏览收费内容（涉及到很多问题，就不放源代码）。
付费漫画，支持原创，支持正版！
付费漫画，支持原创，支持正版！
付费漫画，支持原创，支持正版！