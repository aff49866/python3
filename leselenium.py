from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  #导入Keys

driver = webdriver.Chrome()  #指定使用的浏览器，初始化webdriver
driver.get("https://weibo.com/")  #请求网页地址
driver.maximize_window()
driver.implicitly_wait(5)
user = driver.find_element_by_id("loginname")
pwd = driver.find_element_by_name("password")
user.send_keys("username")  #在搜索框中输入pycon
pwd.send_keys("z")  #相当于回车键，提交
driver.find_element_by_class_name("W_btn_a").click()