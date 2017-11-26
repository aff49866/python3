from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import toutiaopic
import os,time,random
def get_text_word(file_dir):
    text_word_content = []
    dirsort = sorted(os.listdir(file_dir),key=int)
    for i in dirsort:
        sec_file_dir = file_dir + '\\' + i + '\\' + i + '.txt'
        with open(sec_file_dir) as f:
            for r in f.readlines():
                text_word_content.append(r.rstrip('\n'))
    return text_word_content
def file_name(file_dir):
    imagesdir=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                imagesdir.append(os.path.join(root, file))
    return imagesdir
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
def auto_send(driver,send_word_content,upfiles):
    wait = WebDriverWait(driver, 3)  # 页面加载等待时间
    wait.until(EC.presence_of_element_located((By.NAME, 'pic1')))
    upload = driver.find_element_by_name('pic1')
    for files in upfiles:
        upload.send_keys(files) # 上传图片、视频等
    textword = driver.find_element_by_css_selector("textarea[class='W_input']")
    textword.send_keys(send_word_content)  # 文字内容
    wait_upload = WebDriverWait(driver, 1200)
    wait_upload.until_not(EC.presence_of_all_elements_located((By.CLASS_NAME, "loading")))  # 等待上传完成
    time.sleep(3)
    driver.find_element_by_link_text("发布").click()    #点击发布
    driver.refresh()
if __name__ == '__main__':
    file_dir = "I:\\toutiaopic\\" + str(time.strftime("%Y%m%d", time.localtime())) + '\\'
    toutiaopic.main()
    driver = webdriver.Chrome("J:\G盘\python3\chrome\chromedriver.exe") # 指定使用的浏览器，初始化webdriver
    url = 'https://weibo.com/login.php'
    auto_login(driver, url)
    text_word_content = get_text_word(file_dir)
    print(text_word_content)
    for i in range(len(text_word_content)):
        upfiles = file_name(file_dir+ str(i))
        send_word_content = text_word_content[i]
        print(send_word_content,upfiles)
        auto_send(driver, send_word_content, upfiles)
        time.sleep(random.randint(60,600))
    # driver.quit()