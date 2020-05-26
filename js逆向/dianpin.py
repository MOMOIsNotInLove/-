from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# 声明浏览器对象
browser = webdriver.Chrome()
browser.get(
    'https://account.dianping.com/account/iframeLogin?')
wait = WebDriverWait(browser, 10)
# 切换到iframe框架
xf = browser.find_element_by_xpath(r'//*[@id="J_login_container"]/div'/iframe)
browser.switch_to.frame(xf)
# 点击账号登陆按钮，跳过扫码阶段，使用手机号来获取短信来登录
login_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "bottom-password-login")))
login_button.click()
# 获取手机号按钮
mobile_button = wait.until(EC.presence_of_element_located((By.ID, "mobile-number-textbox")))
mobile_button.send_keys("15xxxxxxxxxx")
# 获取验证码按钮节点
verification_button = wait.until(EC.presence_of_element_located((By.ID, "send-number-button")))
verification_button.click()
# 获取验证码输入框
verification_input = wait.until(EC.presence_of_element_located((By.ID, "number-textbox")))
# 休眠一分钟，以便于获取验证码，并及时输入
time.sleep(60)
message = input("请输入你收到的手机验证码:")
verification_input.send_keys(message)

# 获取表单提交按钮的节点位置
submit_button = wait.until(EC.presence_of_all_elements_located((By.ID, "login-button-mobile")))
# 点击提交按钮
submit_button.click()

time.sleep(10)
browser.close()
