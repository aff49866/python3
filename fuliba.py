import requests
from bs4 import BeautifulSoup
import re
# import os
# os.environ['NO_PROXY'] = 'fuliba.net' #不使用代理
def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except ZeroDivisionError as e:
        raise ValueError(e)
def getimg(ulist,html):
    imglist = re.findall(r'http://[\w\d]*?.sinaimg.cn/[\w\d]*?/[\w\d]*?.jpg', html)
    print(imglist)
    soup = BeautifulSoup(html,'html.parser')
    # imgd3 = soup.find_all(title='煎蛋年度妹子图TOP1000')
    for i in soup.find_all(title='煎蛋年度妹子图TOP1000'):
        img = i.attrs['src']
        print(img)
        ulist.append(img)
def main():
    html = gethtml('http://fuliba.net/jd-image-top1000.html')
    ulist = []
    getimg(ulist,html)
main()