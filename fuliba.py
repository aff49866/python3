from threading import Thread
from queue import Queue
from time import sleep
import requests
from bs4 import BeautifulSoup
import time
import os
#q是任务队列
#NUM是并发线程总数
#JOBS是有多少任务
q = Queue()
NUM = 3
JOBS = 10
def geturl(all_link,url): #获取url
    html = gethtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    url_link_list = soup.find_all(rel="bookmark")
    for a in url_link_list:
        link = a.attrs["href"]
        all_link.append([link])
def gethtml(url): #获取html
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except ZeroDivisionError as e:
        raise ValueError(e)
def getimg(ulist,soup): #获取图片
    for i in soup.find_all("p"):
        if i.img != None:
            img = i.img['src']
            ulist.append(img)
def saveimg(ulist): #存取图片到本地电脑
    root = "I:/jiandanpic/"
    for url in ulist:
        path = root + url.split("/")[-1]
        try:
            if not os.path.exists(path):
                imgr = requests.get(url)
                with open(path,'wb') as f:
                    f.write(imgr.content)
            else:
                print("文件已经存在",path)
        except ZeroDivisionError as e:
            raise ValueError(e)
def main(depth_num):
    depth = depth_num
    secend_url_list = []
    ulist = []
    start_time = time.time()
    for l in range(depth):
        url = "http://fuliba.net/page/"
        url = url + str(l+1)
        geturl(secend_url_list, url)
    for n in secend_url_list:
        html = gethtml(n[0])
        soup = BeautifulSoup(html, 'html.parser')
        getimg(ulist, soup)
    saveimg(ulist)
    print("time", time.time() - start_time)
#具体的处理函数，负责处理单个任务
# def do_somthing_using(arguments):
#     print("fdg")
#这个是工作进程，负责不断从队列取数据并处理
def working():
    while True:
        arguments = q.get()
        main(1)
        sleep(1)
        q.task_done()
#fork NUM个线程等待队列
for i in range(NUM):
    t = Thread(target=working)
    t.setDaemon(True)
    t.start()
#把JOBS排入队列
for i in range(JOBS):
    q.put(i)
#等待所有JOBS完成
q.join()