# -*- coding:utf-8 -*-
import requests
import base64
import execjs


class MoMoLogin(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # 将base64字符串还原成图片保存
    def decode_img(self, img_bs64):
        code = img_bs64.replace('data:image/jpg;base64,', '')
        # print code
        x = base64.b64decode(code)
        with open("./yazhengma.jpg", "wb") as f:
            f.write(x)

    def login(self):
        """
        分两次请求：
            1. 携带user,加密的pwd去请求url，返回带图片的二进制的数据的base64进行加密的字符串
            2. 将字符串保存为图片，识别其验证码，再携带上述三个参数去请求同一个url
        :return:
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://web.immomo.com/",
            "Referer": "https://web.immomo.com/"
        }
        url = "https://web.immomo.com/sendCode"
        session = requests.Session()

        with open("./login.js", "r", encoding="utf-8") as f:
            source = f.read()
        ctx = execjs.compile(source=source)
        pwd = ctx.call("getPwd", self.password)
        data = {
            "momoid": self.username,
            "password": pwd,
            "imgv": "",
            "symbol": "/?rf="
        }
        try:
            response = session.post(url=url, data=data, headers=headers, timeout=10)
            if response.status_code == 200:
                img = response.json().get("result")
                self.decode_img(img_bs64=img)
                code = input("请输入相关验证码：").upper()
                data_bs64 = {
                    "momoid": self.username,
                    "password": pwd,
                    "imgv": code,
                    "symbol": "/?rf="
                }
                result = session.post(url=url, data=data_bs64, headers=headers, timeout=10)
                if result.status_code == 200:
                    print(result.json())
        except Exception as e:
            print(e)


if __name__ == '__main__':
    momo = MoMoLogin(username="16530800916", password="chen654321")
    momo.login()
