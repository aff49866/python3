import requests
from bs4 import BeautifulSoup
import bs4,re
def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("err")
def filllist(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    soup.parent
    for tr in soup.find(class_="hidden_zhpm").children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
def printlist(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
def main():
    uinfo=[]
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = gethtml(url)
    filllist(uinfo,html)
    printlist(uinfo,20)
main()
# soupa = soup("li",class_="active")[0]
# soupb = soupa.find_previous_siblings()
# soupb = soup.ul.string
# print(soupb)
# for sibling in soupa:
#     if isinstance(sibling,bs4.element.Tag):
#         print(sibling)
# for i in soup("table","hidden_zhpm"):
#     print(i)
# hidden_zhpm  http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html