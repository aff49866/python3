# import requests
# import urllib.parse
# from bs4 import BeautifulSoup
# import bs4
# def gethtml(url):
#     try:
#         r = requests.get(url)
#         r.raise_for_status()
#         r.encoding = 'utf-8'
#         return r.text
#     except ZeroDivisionError as e:
#         raise ValueError(e)
# html = gethtml("http://fuliba.net/%e6%b0%b8%e4%ba%95%e3%81%bf%e3%81%b2%e3%81%aa.html")
# # print(html)
# soup =BeautifulSoup(html,"html.parser")
# for i in soup.find_all("p"):
#     # print(i)
#     if i.img != None:
#         print(i.img['src'])
# # html = "http://fuliba.net/%e6%b0%b8%e4%ba%95%e3%81%bf%e3%81%b2%e3%81%aa.html"
# # html = urllib.parse.unquote(html) #解码
# # html2 = urllib.parse.quote(html) #编码
# # print(html)
# # print(html2)
import random
def totle(totle):
    a = random.randint(1000,5000)
    b = totle - a
    print(totle,a,b)
totle(5000)