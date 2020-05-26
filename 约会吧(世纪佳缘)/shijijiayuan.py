import requests
import time
import random
import json

"""
目标API：https://search.jiayuan.com/v2/search_v2.php?key=&sex=f&stc=1.11,2:18.23,3:155.170,23:1&sn=default&sv=1&p=1&f=select
`1.11,2:18.23,3:155.170,23:1`:
@:params
1	2	3	4	5	6	7	8	9	10
地区	年龄	身高	学历	月薪	婚史	购房	购车	籍贯	户口
11	12	12	14	15	16	17	18	22	23
民族	宗教信仰	有无子女	职业	公司类型	生肖	星座	血型	诚信等级	照片
————————————————
版权声明：本文为CSDN博主「机灵鹤」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/wenxuhonghe/article/details/83904396 
"""


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/79.0.3945.88 Safari/537.36",
    "referer": "https://login.jiayuan.com/err.php?stolen=right&err_type=-14&pre_url=https://usercp.jiayuan.com/"
}


def get_info(pages):
    try:
        for page in range(1, pages + 1):
            url = "https://search.jiayuan.com/v2/search_v2.php?key=&sex=f&stc=1.11,2:18.24,3:155.170," \
                  "23:1&sn=default&sv=1&p={}&f=select".format(page)
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                info = json.loads(response.text).get("userInfo")
                json_info = response.json().get("userInfo")
                print("\033[1;31m正在打印第%d页数据...\033[0m" % page)
                print(json_info)
            # 设置休眠等待
            random_time = random.randint(1, 4)
            time.sleep(random_time)
            print("======== 休眠：%d秒 =========" % random_time)


    except Exception as e:
        print(e)


if __name__ == '__main__':
    pages = int(input("请输入查询页数："))
    get_info(pages)
