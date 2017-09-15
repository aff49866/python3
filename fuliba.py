import requests
from bs4 import BeautifulSoup
import time
import threading
import os
# os.environ['NO_PROXY'] = 'fuliba.net' #不使用代理
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
def saveimg(ulist):
    root = "I://python//pics//"
    for url in ulist:
        path = root + url.split("/")[-1]
        try:
            if not os.path.exists(path):
                imgr = requests.get(url)
                with open(path,'wb') as f:
                    f.write(imgr.content)
            else:
                print("文件已经存在")
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
        thread = threading.Thread(target=geturl(secend_url_list,url), )
        thread.start()
        thread.join()
    for n in secend_url_list:
        html = gethtml(n[0])
        soup = BeautifulSoup(html, 'html.parser')
        thread2 = threading.Thread(target=getimg(ulist,soup), )
        thread2.start()
        thread2.join()
    saveimg(ulist)
    print("time", time.time() - start_time)
main(1)