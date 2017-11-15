import requests
from bs4 import BeautifulSoup
import re
import os
def readurl(file,urlist):
    with open(file) as f:
        for url in f.readlines():
            urlist.append(url.rstrip('\n'))
def gethtml(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
            'Cookie':'uuid="w:d9390bac4cc14e46be949c5b29caa493"; csrftoken=137a0def4ab5c6da4edd3f9421189163; tt_webid=6453763198302160397; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6453763198302160397; UM_distinctid=15f063fb69b650-06a3d9103aee0c-173b7740-1fa400-15f063fb69c60c; CNZZDATA1259612802=2104685903-1507634371-%7C1510752495; sid_guard="819642177913daed94963a93e332494d|1510671784|15552000|Sun\054 13-May-2018 15:03:04 GMT"; _ga=GA1.2.527974637.1507639396; login_flag=65898838ccf4bec27c491b4428c6411b; sessionid=819642177913daed94963a93e332494d; uid_tt=405a92839a400fa6887c6944cb564d53; sid_tt=819642177913daed94963a93e332494d; _gid=GA1.2.172902799.1510672821; __tasessionId=xfv5g9zrj1510752252792'
        }
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except ZeroDivisionError as e:
        raise ValueError(e)
def getinfo(infolist,html):
    try:
        # soup = BeautifulSoup(html, 'html.parser')
        # imageslist = [i.attrs['href'] for i in soup.select('a.image-origin')]
        # titlelist = [i.text() for i in soup.select("h2.title")]
        titlelist = re.findall("title: '(.*?)'", html)
        imageslist = re.findall(r"\"{\"url\":\"http:\\/\\/p3.pstatp.com\\/origin\\/(.*?)\"\"",html)
        print(titlelist,imageslist)
        # for n in range(len(imageslist)):
        #     images,title = imageslist[n],titlelist[n]
        #     infolist.append([images,title])
        # print(infolist)
    except ZeroDivisionError as e:
        raise ValueError(e)
def saveinfo(infolist,pagenum,html):
    # os.chdir(r"I:/toutiaopic/")
    # os.mkdir(str(pagenum))

    for c in range(len(infolist)):
        print(c)
        os.mkdir(r"I:/toutiaopic/" + str(pagenum))
        for n in infolist[c][0]:
            # root = "I:/toutiaopic"
            path = n.split("/")[-1]
            try:
                if not os.path.exists(path):
                    imgr = requests.get(n)
                    with open(path, 'wb') as f:
                        f.write(imgr.content)
                else:
                    print("文件已经存在", path)
            except ZeroDivisionError as e:
                raise ValueError(e)
if __name__ == '__main__':
    file = "I:/toutiaopic/picimages.txt"
    urlist,infolist=[],[]
    readurl(file,urlist)
    for l in range(len(urlist)):
        html = gethtml(urlist[l])
        getinfo(infolist,html)
        print(infolist)
        # saveinfo(infolist,pagenum=l)

