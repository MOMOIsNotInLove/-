# -*- coding:utf-8 -*-


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import base64
from PIL import Image
from io import BytesIO

USERNAME = '15867119504'
PASSWARD = 'chen123456'
BORDER = 12
INIT_LEFT = 60


class loginBili():
    def __init__(self):
        self.url = 'https://passport.bilibili.com/login'  # B站登录界面
        # 创建chrome参数对象
        chrome_options = webdriver.ChromeOptions()
        # 设置为开发者模式
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(options=chrome_options)
        # 定义显示等待
        self.wait = WebDriverWait(self.browser, 20)
        self.username = USERNAME
        self.password = PASSWARD

    # def __del__(self):
    #     # 关闭浏览器
    #     self.browser.close()

    def login_successfully(self):
        """
        判断是否登陆成功
        :return:
        """
        try:
            # 登录成功后 界面上会有一个消息按钮
            return bool(
                WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//span[text()="消息"]')))
            )
        except TimeoutException:
            print('超时了!!!')
            return False

    def move_to_gap(self, track):
        """
        拖动滑块到缺口处
        :param track: 轨迹
        :return:
        """
        # 按住滑块
        slider = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_slider_button')))
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            # 只有水平方向有运动 按轨迹移动
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()  # 松开鼠标

    def get_track(self, distance):
        """
        根据偏移量 获取移动轨迹
        :param gap: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        trace = []
        # 设置加速距离为总距离的4/5
        faster_distance = distance * (4 / 5)
        # 设置初始位置、初始速度、时间间隔
        start, v0, t = 0, 0, 0.4
        while start < distance:
            if start < faster_distance:
                a = 10
            else:
                a = -10
            # 位移
            move = v0 * t + 1 / 2 * a * t * t
            # 当前时刻的速度
            v = v0 + a * t
            v0 = v
            start += move
            trace.append(move)
        # trace 记录了每个时间间隔移动了多少位移
        return trace

    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两张图片 各个位置的像素是否相同
        :param image1:不带缺口的图片
        :param image2: 带缺口的图片
        :param x: 位置x
        :param y: 位置y
        :return: (x,y)位置的像素是否相同
        """
        # 获取两张图片指定位置的像素点
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        # 设置一个阈值 允许有误差
        threshold = 10
        # 彩色图 每个位置的像素点有三个通道
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
                pixel1[2] - pixel2[2]) < threshold:
            return True
        return False

    def get_gap(self, image1, image2):
        """
        获取缺口偏移量
        :param image1:不带缺口的图片
        :param image2: 带缺口的图片
        :return:
        """
        left = INIT_LEFT  # 定义一个左边的起点 缺口一般离图片左侧有一定的距离 有一个滑块
        for i in range(INIT_LEFT, image1.size[0]):  # 从左到右 x方向
            for j in range(image1.size[1]):  # 从上到下 y方向
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i  # 找到缺口的左侧边界 在x方向上的位置
                    return left
        return left

    def get_geetest_image(self):
        """
        获取验证码图片
        :return: 图片对象
        """
        # # 带滑块和阴影的图片
        # im = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.geetest_canvas_bg')))
        # im.screenshot('image.png')
        time.sleep(1)
        # 执行 JS 代码并拿到完整图 base64 数据
        JS = 'return document.getElementsByClassName("geetest_canvas_fullbg")[0].toDataURL("image/png");'
        im_info = self.browser.execute_script(JS)
        # print(im_info)
        # 拿到base64编码的图片信息
        im_base64 = im_info.split(',')[1]
        # 转为bytes类型
        image1 = base64.b64decode(im_base64)
        # 加载图片
        image1 = Image.open(BytesIO(image1))
        # 保存图片
        image1.save('image1.png')
        # 执行 JS 代码并拿到只带阴影图 base64 数据
        JS = 'return document.getElementsByClassName("geetest_canvas_bg")[0].toDataURL("image/png");'
        im_info = self.browser.execute_script(JS)
        # print(im_info)
        # 拿到base64编码的图片信息
        im_base64 = im_info.split(',')[1]
        # 转为bytes类型
        image2 = base64.b64decode(im_base64)
        # 加载图片
        image2 = Image.open(BytesIO(image2))
        # 保存图片
        image2.save('image2.png')
        return image1, image2

    def get_login_btn(self):
        """
        登陆
        :return: None
        """
        # 打开网址
        self.browser.get(self.url)
        # 找到用户名输入框,在浏览器中定位它的HTML代码后 根据id属性来找
        username = self.wait.until(EC.presence_of_element_located((By.ID, 'login-username')))
        # 找到密码输入框
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'login-passwd')))
        # 输入用户名和密码
        username.send_keys(self.username)
        time.sleep(2)
        password.send_keys(self.password)
        time.sleep(2)
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-login')))
        return button

    def run(self):
        # 输入用户名和密码并点击登录按钮
        self.get_login_btn().click()
        # 获取验证码图片
        image1, image2 = self.get_geetest_image()
        # 找到缺口的左侧边界 在x方向上的位置
        gap = self.get_gap(image1, image2)
        print('缺口位置：', gap)
        # 减去滑块左侧距离图片左侧在x方向上的距离 即为滑块实际要移动的距离
        gap -= BORDER
        # 获取移动轨迹
        track = self.get_track(gap)
        print('滑动轨迹：', track)
        # 按轨迹拖动滑块
        self.move_to_gap(track)
        if self.login_successfully():
            print("登录成功")
        else:
            print('正在重试.....')
            self.run()


if __name__ == '__main__':
    login = loginBili()
    login.run()
