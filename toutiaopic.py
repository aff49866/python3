import requests
import re
import os,time
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
        r.encoding = 'utf-8'
        return r.text
    except ZeroDivisionError as e:
        raise ValueError(e)
def getinfo(infolist,html,title):
    try:
        reg = re.compile(r"title: '(.*?)'", re.S)
        reg2 = re.compile(r'/origin\\\\/(\w+)\\', re.S)
        title.append(reg.findall(html)[0])
        imagesmore = reg2.findall(html)
        imageslist = sorted(set(imagesmore), key=imagesmore.index)
        for i in imageslist:
            imageurl = "http://p1.pstatp.com/origin/" + i
            infolist.append(imageurl)
    except ZeroDivisionError as e:
        raise ValueError(e)
def saveinfo(infolist,title,pathconfig,pagenum):
    os.makedirs(pathconfig + str(time.strftime("%Y%m%d", time.localtime())) + '\\' + str(pagenum))
    for e in infolist:
        path = pathconfig + str(time.strftime("%Y%m%d", time.localtime())) + '\\' + str(pagenum) + '\\'+ e.split("/")[-1] + '.jpg'
        print(path)
        try:
            imgr = requests.get(e)
            with open(path, 'wb') as f:
                f.write(imgr.content)
        except ZeroDivisionError as e:
            raise ValueError(e)
    try:
        textpath = pathconfig + str(time.strftime("%Y%m%d", time.localtime())) + '\\' + str(pagenum) + '\\' + str(pagenum) + '.txt'
        print(textpath)
        with open(textpath, 'w',encoding='utf-8') as f:
            f.write(str(title[0]))
    except ZeroDivisionError as e:
        raise ValueError(e)
def main(pathconfig):
    file = pathconfig + '\picimages.txt' #url地址，比如：https://www.toutiao.com/a6471196162622751245
    urlist,infolist,title=[],[],[]
    readurl(file,urlist)
    for l in range(len(urlist)):
        html = gethtml(urlist[l])
        getinfo(infolist,html,title)
        print(infolist,title)
        saveinfo(infolist,title,pathconfig,pagenum=l)
        infolist,title=[],[]