from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  #导入Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
account = input() #输入账号
password = input() #输入密码
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# service_args=[]
# service_args.append('--load-images=no')  ##关闭图片加载
driver = webdriver.PhantomJS("I:\python\phantomjs\phantomjs.exe",desired_capabilities=dcap)  #指定使用的浏览器，初始化webdriver
t1 = time.time()
driver.get("https://weibo.com/login.php")  #请求网页地址
# driver.implicitly_wait(5)
element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.ID, "loginname"))
    )
# driver = webdriver.Chrome('J:/G盘/python3/chrome/chromedriver.exe')  #指定使用的浏览器，初始化webdriver
driver.maximize_window()
driver.implicitly_wait(5)
user = driver.find_element_by_id("loginname")
pwd = driver.find_element_by_name("password")
user.send_keys(account)  #在搜索框中输入pycon
pwd.send_keys(password)  #相当于回车键，提交
driver.find_element_by_class_name("W_btn_a").click()  #提交
# upload = driver.find_element_by_name('pic1')
# upload.send_keys(r"J:\G盘\python3\ufeg.jpg")
driver.save_screenshot("abd2.png")
driver.quit()
t = time.time()-t1
print(t)

