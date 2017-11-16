import requests
import re
def gethtml(url):
    headers = {
                "Cookie":'uuid="w:f32cbfdbc47443459d49539692047bb8"; csrftoken=2203d2853f1b2c6885495cc467dd87b5; _ba=BA0.2-20171017-51d9e-ZIuNA0TlmvsH5Ty4swwE; tt_webid=60660399197; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=8puv4a7za1510817224326',
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    r = requests.get(url,headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
    return r.text
def getinfo(infolist,html):
    reg = re.compile(r"title: '(.*?)'",re.S)
    reg2 = re.compile(r'/origin\\\\/(\w+)\\', re.S)
    title = reg.findall(html)[0]
    imagesmore = reg2.findall(html)
    imageslist = sorted(set(imagesmore),key=imagesmore.index)
    for i in imageslist:
        imageurl = "http://p1.pstatp.com/origin/" + i
        infolist.append(imageurl)
    print(infolist)
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
if __name__== '__main__':
    url = 'https://www.toutiao.com/a6474565290091872782/'
    infolist = []
    html = gethtml(url)
    getinfo(infolist,html)