from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def auto_login(driver,url):
    account = input() #输入账号
    password = input() #输入密码
    driver.get(url)  # 请求网页地址
    # driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 3)  # 页面加载等待时间
    wait.until(EC.title_contains("微博"))
    driver.set_window_size(1920, 1080)
    wait.until(EC.presence_of_element_located((By.ID, 'loginname')))  # 等待出现id为loginname的元素载入完成
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'W_btn_a')))  # 等待出现class为W_btn_a的元素可以点击
    driver.find_element_by_id("loginname").send_keys(account) # 在搜索框中输入帐号
    driver.find_element_by_name("password").send_keys(password)# 输入密码
    driver.find_element_by_class_name("W_btn_a").click()  # 提交
def auto_send(driver,*upfiles):
    wait = WebDriverWait(driver, 3)  # 页面加载等待时间
    wait.until(EC.presence_of_element_located((By.NAME, 'pic1')))
    upload = driver.find_element_by_name('pic1')
    for files in upfiles:
        upload.send_keys(files) # 上传图片、视频等
    textword = driver.find_element_by_css_selector("textarea[class='W_input']")
    textword.send_keys("上传多张图片上传多张图片上传多张图片上传多张图片")  # 文字内容
    wait_upload = WebDriverWait(driver, 30000)
    wait_upload.until_not(EC.presence_of_all_elements_located((By.CLASS_NAME, "loading")))  # 等待上传完成
    driver.find_element_by_link_text("发布").click()    #点击发布
    driver.quit()
if __name__ == '__main__':
    driver = webdriver.Chrome("J:\G盘\python3\chrome\chromedriver.exe") # 指定使用的浏览器，初始化webdriver
    url = 'https://weibo.com/login.php'
    upfile1 =r"I:\python\git\python3\python3\abd2.png"
    upfile2 =r"J:\G盘\python3\python3\VCG21gic19976029.jpg"
    auto_login(driver,url)
    auto_send(driver,upfile1,upfile2)