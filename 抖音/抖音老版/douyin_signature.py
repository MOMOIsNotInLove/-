# -*- coding:utf-8 -*-
import execjs
from selenium import webdriver

tac = 'i)6a3k9eqmes!i#3bqs"0y\u02a1g,&qnfme|ms g,)gk}ejo{\x7fcms!g,&Iebli\x7fms"l!,)~oih\x7fgyucmk"t (\x80,' \
      '.jjvx|vDgyg}knbl"d"inkfl"v,.jjvx|vDgyg}knbmxl!,)~oih\x7fgyucgr&Objectn vuq%valuevfq(writable[#c}) %{s#t ,' \
      '4KJarz}hrjxl@EWCOQDRB,3LKfs{}wsnqB{iAMWBP@,;DCj{}DSKUAWyTK[C[XrHZ^RFZ[[,7HGn\x7fyxowiES}PGWOW\\vL^BN,' \
      '5JI`}{~iuk{m\x7fRAQMURxNG,3LKsnsjpl~nB{iAMWBP@,2MLpg\x7fa}kEnrjl~PQGG,5JI`}{~iuk{m\x7fTLTVDVWMM,' \
      '1NMwf|`rjF\x7fm}qk~TD,4KJert|tripAjNVPBTUCC,4KJpo|ksmyoAjNVPBTUCC[+s#,)Vyn`h`fe|,,olbcCt~vz|cz,' \
      '6ID}u\x7fuuhs@ieg|v@EHZMOY[#s$l$*%s%l%u&k4s&l$l&ms\'l l\'mk"t j\x06l#*%s%l%u&k?s&l#l&ms\'l ,(lfi~ah`{ml\'mk"t ' \
      'j\ufffbl ,(lfi~ah`{m*%s%l%u&kls&l&vr%matchxgr&RegExp$*\\$[a-z]dc_$ n"[!cvk:}l ,(lfi~ah`{ml&m,&efkaoTmk"t ' \
      'j\uffcef z[ cb|1d<,%Dscafgd"in,8[xtm}nLzNEGQMKAdGG^NTY\x1ckgd"inb<b|1d<g,&TboLr{m,(\x02)!jx-2n&vr$testxg,' \
      '%@tug{mn ,%vrfkbm[!cb|'
user_id = "80813608394"


def get_signature():
    # compile 编译执行复杂的js源代码
    with open("./signature_demo.js", 'r', encoding="gbk") as f:
        resource = f.read()

    browser = webdriver.Chrome()
    browser.get("https://www.baidu.com")
    print(browser.execute_script(resource, tac, user_id))
    # x = execjs.compile(resource, cwd=r"C:\Users\CHD\AppData\Roaming\npm\node_modules")
    # # 执行目标函数
    # result = x.call("getSignature", tac, user_id)  # 1587110199832
    # print(result)


if __name__ == '__main__':
    get_signature()
