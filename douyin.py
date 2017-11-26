from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import re
import os,time
def readurl(file,urlist):
    with open(file) as f:
        for url in f.readlines():
            urlist.append(url.rstrip('\n'))
    return urlist
def gethtml(url,urlist):
    try:
        driver.get(url)
        driver.set_window_size(1920, 1080)
        wait = WebDriverWait(driver, 600)  # 页面加载等待时间
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'btn')))
        for list in urlist:
            driver.find_element_by_class_name('link-input').send_keys(list)
            driver.find_element_by_css_selector('button.btn').click()
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'btn-success')))
            videourl = driver.find_element_by_css_selector('a.btn-success').get_attribute('href')
            imgurl = driver.find_element_by_css_selector('a.btn-info').get_attribute('href')
            videolist = [videourl,imgurl]
            print(videolist,urlist.index(list))
            os.makedirs(r"I:/douyin/" + str(time.strftime("%Y%m%d", time.localtime())) + '/' + str(urlist.index(list)))
            path = r"I:/douyin/" + str(time.strftime("%Y%m%d", time.localtime())) + '/' + str(urlist.index(list))
            try:
                video = requests.get(videolist[0])
                videosplit = re.split(r"/|.|\?", videolist[0])
                print(videosplit)
                print(path+'/'+ videosplit[-3] + '.mp4')
                with open(path+'/'+ videosplit[-3] + '.mp4', 'wb') as f:
                    f.write(video.content)
                images = requests.get(videolist[1])
                with open(path + '/' + videolist[1].split("/")[-1], 'wb') as f:
                    f.write(images.content)
            except ZeroDivisionError as e:
                raise ValueError(e)
    # + str(pagenum) + '/' + e.split("/")[-1] + '.jpg'
    except ZeroDivisionError as e:
         raise ValueError(e)
def savevideo():
    pass
if __name__=='__main__':
    # service_args = []
    # service_args.append('--load-images=false')
    # service_args.append('--disk-cache=true')
    # service_args.append('--ignore-ssl-errors=true')
    # service_args.append('--ssl-protocol=TLSv1')
    # headers = {'Host':'service.iiilab.com',
    #             'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    #             'Accept':'application/json, text/javascript, */*; q=0.01',
    #             'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    #             'Accept-Encoding':'gzip, deflate',
    #             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    #             'Origin':'http://douyin.iiilab.com',
    #             'Cookie':'_ga=GA1.2.2051238493.1507653212; _gid=GA1.2.1646775579.1511609661; PHPSESSIID=470223315116; _gat=1',
    #             'Connection':'keep-alive'
    #            }
    # for key, value in enumerate(headers):
    #     capability_key = 'phantomjs.page.customHeaders.{}'.format(key)
    #     webdriver.DesiredCapabilities.PHANTOMJS[capability_key] = value
    # driver = webdriver.PhantomJS("I:\phantomjs.exe",service_args=service_args)
    driver = webdriver.Chrome('J:\G盘\python3\chrome\chromedriver.exe')
    file = "I:/douyin/douyin.txt"
    urlist = []
    urlist = readurl(file,urlist)
    url = 'http://douyin.iiilab.com/'
    gethtml(url,urlist)