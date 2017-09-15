import requests
from bs4 import BeautifulSoup
import re
# import os
# os.environ['NO_PROXY'] = 'fuliba.net' #不使用代理
def geturl(all_link,url):
    html = gethtml(url)
    soup = BeautifulSoup(html, 'html.parser')
    url_link_list = soup.find_all(rel="bookmark")
    for a in url_link_list:
        link = a.attrs["href"]
        all_link.append([link])
def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except ZeroDivisionError as e:
        raise ValueError(e)
def getimg(ulist,soup):
    for i in soup.find_all("p"):
        if i.img != None:
            img = i.img['src']
            ulist.append(img)
def printimg(ulist):
    for u in ulist:
        print(u)
def main(depth_num):
    depth = depth_num
    secend_url_list = []
    for l in range(depth):
        url = "http://fuliba.net/page/"
        url = url + str(l+1)
        geturl(secend_url_list,url)
    ulist = []
    for n in secend_url_list:
        html = gethtml(n[0])
        soup = BeautifulSoup(html, 'html.parser')
        getimg(ulist,h,soup)
    printimg(ulist)
main(3)