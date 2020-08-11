### 咪咕登录js逆向破解

> MiGu登录参数分析 参考文章：https://cuiqingcai.com/9549.html

**浏览器函数：**
当我们进行js逆向，执行js函数时，有一些浏览器参数是无法模拟出来的，比如**window，navigator，location**等

```javascript
navigator = {};
window = this;
```

- 获取publicExponent，modulus的url：https://passport.migu.cn/password/publickey

- 登录url：https://passport.migu.cn/authn

   - 请求参数
```
sourceID: 208003（固定值）
appType: 0（固定值）
relayState: 
loginID: 加密方式一
enpassword: 加密方式一
captcha: 
imgcodeType: 1（固定值）
rememberMeBox: 1（固定值）
fingerPrint: 加密方式二
fingerPrintDetail: 加密方式三
isAsync: true
```