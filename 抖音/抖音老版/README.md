## 抖音_signature算法

**抖音网页版获取用户的所有的作品：** 主要参考这篇文章：https://mp.weixin.qq.com/s/3r8yVDZ0lKrgot3XV6-8cA

用户列表的作品的API接口：
```text
https://www.iesdouyin.com/web/api/v2/aweme/post/
?user_id=102777167489
&sec_uid=&count=21
&max_cursor=0
&aid=1128
&_signature=jaSBxRAd029lfqO4ZaLPGo2kgd&dytk=373c0c83cf5a69b82a5264f3482103d9
```

获取_signature主要是根据用户id与tac值
```html
<!DOCTYPE html>
<html style="font-size: 50px;">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>抖音_signature破解</title>
</head>
<body>
    <input type="text" id="url"/>
    <div id="sign"></div>

<script src="./Signature.js"></script>
<script>
    window.onload = function () {
        let tac = 'i)6a41sg5vps!i$15rjs"0y\u02a1g,&qnfme|ms g,)gk}ejo{\x7fcms!g,&Iebli\x7fms"l!,)~oih\x7fgyucmk"t (\x80,.jjvx|vDgyg}knbl"d"inkfl"v,.jjvx|vDgyg}knbmxl!,)~oih\x7fgyucgr&Objectn vuq%valuevfq(writable[#c}) %{s#t ,4KJarz}hrjxl@EWCOQDRB,3LKfs{}wsnqB{iAMWBP@,;DCj{}DSKUAWyTK[C[XrHZ^RFZ[[,7HGn\x7fyxowiES}PGWOW\\vL^BN,5JI`}{~iuk{m\x7fRAQMURxNG,3LKsnsjpl~nB{iAMWBP@,2MLpg\x7fa}kEnrjl~PQGG,5JI`}{~iuk{m\x7fTLTVDVWMM,1NMwf|`rjF\x7fm}qk~TD,4KJert|tripAjNVPBTUCC,4KJpo|ksmyoAjNVPBTUCC[+s#,)Vyn`h`fe|,,olbcCt~vz|cz,6ID}u\x7fuuhs@ieg|v@EHZMOY[#s$l$*%s%l%u&k4s&l$l&ms\'l l\'mk"t j\x06l#*%s%l%u&k?s&l#l&ms\'l ,(lfi~ah`{ml\'mk"t j\ufffbl ,(lfi~ah`{m*%s%l%u&kls&l&vr%matchxgr&RegExp$*\\$[a-z]dc_$ n"[!cvk:}l ,(lfi~ah`{ml&m,&efkaoTmk"t j\uffcef z[ cb|1d<,%Dscafgd"in,8[xtm}nLzNEGQMKAdGG^NTY\x1ckgd"inb<b|1d<g,&TboLr{m,(\x02)!jx-2n&vr$testxg,%@tug{mn ,%vrfkbm[!cb|';
        let user_id = "102777167489";
        document.getElementById("sign").innerText = getSignature(tac, user_id)
    };
</script>
</body>
</html>
```

抖音的signature.js

```javascript
function getSignature(_tac, userId) {
    tac = _tac;
    var e = {};
    webdriver = "D:\\data\\master\\spider案例\\抖音\\chromedriver.exe";
    var r = (function () {
        function e(e, a, r) {
            return (b[e] || (b[e] = t("x,y", "return x " + e + " y")))(r, a)
        }

        function a(e, a, r) {
            return (k[r] || (k[r] = t("x,y", "return new x[y](" + Array(r + 1).join(",x[++y]").substr(1) + ")")))(e, a)
        }

        function r(e, a, r) {
            var n, t, s = {}, b = s.d = r ? r.d + 1 : 0;
            for (s["$" + b] = s,
                     t = 0; t < b; t++)
                s[n = "$" + t] = r[n];
            for (t = 0,
                     b = s.length = a.length; t < b; t++)
                s[t] = a[t];
            return c(e, 0, s)
        }

        function c(t, b, k) {
            function u(e) {
                v[x++] = e
            }

            function f() {
                return g = t.charCodeAt(b++) - 32,
                    t.substring(b, b += g)
            }

            function l() {
                try {
                    y = c(t, b, k)
                } catch (e) {
                    h = e,
                        y = l
                }
            }

            for (var h, y, d, g, v = [], x = 0; ;)
                switch (g = t.charCodeAt(b++) - 32) {
                    case 1:
                        u(!v[--x]);
                        break;
                    case 4:
                        v[x++] = f();
                        break;
                    case 5:
                        u(function (e) {
                            var a = 0
                                , r = e.length;
                            return function () {
                                var c = a < r;
                                return c && u(e[a++]),
                                    c
                            }
                        }(v[--x]));
                        break;
                    case 6:
                        y = v[--x],
                            u(v[--x](y));
                        break;
                    case 8:
                        if (g = t.charCodeAt(b++) - 32,
                            l(),
                            b += g,
                            g = t.charCodeAt(b++) - 32,
                        y === c)
                            b += g;
                        else if (y !== l)
                            return y;
                        break;
                    case 9:
                        v[x++] = c;
                        break;
                    case 10:
                        u(s(v[--x]));
                        break;
                    case 11:
                        y = v[--x],
                            u(v[--x] + y);
                        break;
                    case 12:
                        for (y = f(),
                                 d = [],
                                 g = 0; g < y.length; g++)
                            d[g] = y.charCodeAt(g) ^ g + y.length;
                        u(String.fromCharCode.apply(null, d));
                        break;
                    case 13:
                        y = v[--x],
                            h = delete v[--x][y];
                        break;
                    case 14:
                        v[x++] = t.charCodeAt(b++) - 32;
                        break;
                    case 59:
                        u((g = t.charCodeAt(b++) - 32) ? (y = x,
                            v.slice(x -= g, y)) : []);
                        break;
                    case 61:
                        u(v[--x][t.charCodeAt(b++) - 32]);
                        break;
                    case 62:
                        g = v[--x],
                            k[0] = 65599 * k[0] + k[1].charCodeAt(g) >>> 0;
                        break;
                    case 65:
                        h = v[--x],
                            y = v[--x],
                            v[--x][y] = h;
                        break;
                    case 66:
                        u(e(t[b++], v[--x], v[--x]));
                        break;
                    case 67:
                        y = v[--x],
                            d = v[--x],
                            u((g = v[--x]).x === c ? r(g.y, y, k) : g.apply(d, y));
                        break;
                    case 68:
                        u(e((g = t[b++]) < "<" ? (b-- ,
                            f()) : g + g, v[--x], v[--x]));
                        break;
                    case 70:
                        u(!1);
                        break;
                    case 71:
                        v[x++] = n;
                        break;
                    case 72:
                        v[x++] = +f();
                        break;
                    case 73:
                        u(parseInt(f(), 36));
                        break;
                    case 75:
                        if (v[--x]) {
                            b++;
                            break;
                        }
                    case 74:
                        g = t.charCodeAt(b++) - 32 << 16 >> 16,
                            b += g;
                        break;
                    case 76:
                        u(k[t.charCodeAt(b++) - 32]);
                        break;
                    case 77:
                        y = v[--x],
                            u(v[--x][y]);
                        break;
                    case 78:
                        g = t.charCodeAt(b++) - 32,
                            u(a(v, x -= g + 1, g));
                        break;
                    case 79:
                        g = t.charCodeAt(b++) - 32,
                            u(k["$" + g]);
                        break;
                    case 81:
                        h = v[--x],
                            v[--x][f()] = h;
                        break;
                    case 82:
                        u(v[--x][f()]);
                        break;
                    case 83:
                        h = v[--x],
                            k[t.charCodeAt(b++) - 32] = h;
                        break;
                    case 84:
                        v[x++] = !0;
                        break;
                    case 85:
                        v[x++] = void 0;
                        break;
                    case 86:
                        u(v[x - 1]);
                        break;
                    case 88:
                        h = v[--x],
                            y = v[--x],
                            v[x++] = h,
                            v[x++] = y;
                        break;
                    case 89:
                        u(function () {
                            function e() {
                                return r(e.y, arguments, k)
                            }

                            return e.y = f(),
                                e.x = c,
                                e
                        }());
                        break;
                    case 90:
                        v[x++] = null;
                        break;
                    case 91:
                        v[x++] = h;
                        break;
                    case 93:
                        h = v[--x];
                        break;
                    case 0:
                        return v[--x];
                    default:
                        u((g << 16 >> 16) - 16)
                }
        }

        var n = this
            , t = n.Function
            , s = Object.keys || function (e) {
            var a = {}
                , r = 0;
            for (var c in e)
                a[r++] = c;
            return a.length = r,
                a
        }
            , b = {}
            , k = {};
        return r
    })()('gr$Daten Иb/s!l y͒yĹg,(lfi~ah`{mv,-n|jqewVxp{rvmmx,&effkx[!cs"l".Pq%widthl"@q&heightl"vr*getContextx$"2d[!cs#l#,*;?|u.|uc{uq$fontl#vr(fillTextx$$龘ฑภ경2<[#c}l#2q*shadowBlurl#1q-shadowOffsetXl#$$limeq+shadowColorl#vr#arcx88802[%c}l#vr&strokex[ c}l"v,)}eOmyoZB]mx[ cs!0s$l$Pb<k7l l!r&lengthb%^l$1+s$jl  s#i$1ek1s$gr#tack4)zgr#tac$! +0o![#cj?o ]!l$b%s"o ]!l"l$b*b^0d#>>>s!0s%yA0s"l"l!r&lengthb<k+l"^l"1+s"jl  s&l&z0l!$ +["cs\'(0l#i\'1ps9wxb&s() &{s)/s(gr&Stringr,fromCharCodes)0s*yWl ._b&s o!])l l Jb<k$.aj;l .Tb<k$.gj/l .^b<k&i"-4j!+& s+yPo!]+s!l!l Hd>&l!l Bd>&+l!l <d>&+l!l 6d>&+l!l &+ s,y=o!o!]/q"13o!l q"10o!],l 2d>& s.{s-yMo!o!]0q"13o!]*Ld<l 4d#>>>b|s!o!l q"10o!],l!& s/yIo!o!].q"13o!],o!]*Jd<l 6d#>>>b|&o!]+l &+ s0l-l!&l-l!i\'1z141z4b/@d<l"b|&+l-l(l!b^&+l-l&zl\'g,)gk}ejo{cm,)|yn~Lij~em["cl$b%@d<l&zl\'l $ +["cl$b%b|&+l-l%8d<@b|l!b^&+ q$sign ', [e])
    return e.sign(userId)
}
```

接下来注意了，应用python的execjs库，**将tac，userid代入signature算法中传入js中，发现运行错误，而放在html中运行则正常，查资料后发现是在js中没有window对象，于是在js中将tac定义为global对象，结果运行报错。照理说应该都是一样的啊！！！！！**
于是便尝试了python一些js执行库如pyexecjs，结果都是这样：不加tac运行参数错误，而加入tac值后运行报错。在HTML运行是加入tac值后，运行结果是固定的，而在node等运行时结果是不同的，应是有根据时间生成参数值，而在tac值中就有时间。

<fancybox>![](https://img-blog.csdnimg.cn/2020030316075336.png)</fancybox>

于是便觉得是必须要使用浏览器运行才是正确的，辗转之后试了一下phantomjs运行，发现与正确的参数值大致相同，只有中间几位数与后面一位数不同，但是使用这个参数无法请求成功。无奈选择使用selenium尝试，结果运行结果与使用phantomjs运行结果都是有几个字母不同。这是在js中有特征值识别，在运行加密js之前将window.navigator.webdriver设置为undefined，结果正常手动打开网页都得到错误的加密值。




注意点：
1. headers一律使用移动端的user-agent，不要使用PC端的user-agent
2. 无法一次性把用户所有的数据获取到，**只能分页获取**，并且这个参数max_cursor 是关键，第一次默认传0，请求成功后返回值里面会有max_cursor，下一次请求则传上一次请求所返回的max_cursor