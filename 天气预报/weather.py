import re
import requests
from tqdm import tqdm
from pyquery import PyQuery as pq
import execjs
"""
天气预报数据爬取，整理数据:
1. 经过发现，可以直接在网页上获取数据(更正：网页源代码有问题，无法获取数据)
2. 数据API接口，可以获取数据

"""


def get_url():
    """
    构造目标请求的url
    :param province:代表省份（大写的拼音简写 四川：SC）
    :param city: 目标城市（小写的拼音 绵阳：mianyang）
    :return:URL
    """
    province = input("请输入查询的省份（大写的拼音简写 四川：SC）：")
    city = input("请输入查询的城市（小写的拼音 绵阳：mianyang）：")
    pattern = re.compile("[A-Za-z]+")
    if len(re.search(pattern, province).group(0)) > 2:
        print("\033[1;42;31m输入城市错误，请核查。。。\033[0m")
        return None
    else:
        province = province.upper().strip()
        city = (re.search(pattern, city).group(0)).lower().strip()
        url = "http://www.nmc.cn/publish/forecast/A{}/{}.html".format(province, city)
        print("\033[1;31m目标url构建成功：\033[0m", url)
        return url


def get_info():
    headers = {
        "Host": "www.nmc.cn",
        "Referer": "http://www.nmc.cn/publish/forecast/ANX/dawukou.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "Cookie":"td_cookie=205513882; td_cookie=205285986; UM_distinctid=171860f6de84c1-0d08c1f29f53f5-6701b35-144000-171860f6de98cc; CNZZDATA1254743953=1049407370-1587089013-%7C1587101459; ray_leech_token=1587106355"
    }
    url = "http://www.nmc.cn/publish/forecast/ASC/mianyang.html"
    try:
        response = requests.get(url=url, headers=headers, timeout=10)
        if response.status_code == 200:
            print(response.text)
            # 将返回数据进行pyquery初始化
            doc = pq(response.text)
            # 遍历目标节点
            print()
            items = doc(".pull-left.weather .weatherWrap").items()
            for item in items:
                date = item.find("div").eq(0).text()    # 日期
                weather_icon = item.find("div").eq(1).find("img").attr("src")    # 天气图标
                desc = item.find("div").eq(2).text()    # 天气情况
                windd = item.find("div").eq(3).text()    # 风向
                winds = item.find("div").eq(4).text()    # 风力
                max_tmp = item.find("div").eq(5).text()    # 最高温度
                min_tmp = item.find("div").eq(6).text()    # 最低温度
                weather_icon2 = item.find("div").eq(7).find("img").attr("src")    # 天气图标2
                desc2 = item.find("div").eq(8).text()  # 天气情况
                windd2 = item.find("div").eq(9).text()  # 风向
                winds2 = item.find("div").eq(10).text()  # 风力
                print(date+" "+weather_icon+" "+desc+" "+windd+" "+winds+" "+max_tmp+" "+min_tmp)
                print(weather_icon2+" "+desc2+" "+windd2+" "+winds2)
                print("===========================================")

            print(items)
    except Exception as e:
        print(e)


def get_mess():
    """
    由于之前无法通过网页源代码获取数据，经过发现，找到了如下几个API
    api_1:http://www.nmc.cn/rest/province/ASC?_=1587103476309 (查询字符串，必须带有“？”号，表示毫秒级时间戳)
    api_2:http://www.nmc.cn/rest/weather?stationid=53903&_=1587103476307
    api_3:http://www.nmc.cn/rest/province/all?_=1587103476306
    :param api_1:先通过api_1的http://www.nmc.cn/rest/province/A（大写的省份首字母简写） 来获取目标省份下的城市编码code
    :param api_2:在api_1获取的code编码后，构建新的api_2的http://www.nmc.cn/rest/weather?stationid=（城市编码code） 来获取目标城市的具体天气数据
    :param api_3:直接展示所有的省份以及其编码
    :return:
    """
    js = """
    function get_time(){
        let d = new Date();
        return d.getTime();
    }
    """""
    times = execjs.compile(js).call("get_time")
    print(times)



if __name__ == '__main__':
    get_mess()
