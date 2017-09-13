import re,requests
def gethtml(url):
    try:
        r = requests.get(url,timeout=30)
        r.request
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("page")
def getcon(ulist,html):
    try:
        pricelist = re.findall(r'"view_price":"[\d\.]*"' , html)
        titlelist = re.findall(r'"raw_title":".*?"' , html)
        for i in range(len(pricelist)):
            price = eval(pricelist[i].split(":")[1])
            title = eval(titlelist[i].split(":")[1])
            ulist.append([price,title])
    except:
        print("获取内容失败")
def printgood(ulist):
    tplist = "{:4}\t{:8}\t{:16}\t"
    print(tplist.format("序号","价格","商品名称"))
    count = 0
    for t in ulist:
        count+=1
        print(tplist.format(count,t[0],t[1]))
def main():
    goods = "电脑"
    url = "https://s.taobao.com/search?q=" + goods
    depth = 3
    infolist = []
    for n in range(depth):
        try:
            url = url + "&s=" + str(44*n)
            html = gethtml(url)
            getcon(infolist,html)
        except:
            print("main")
    printgood(infolist)
main()