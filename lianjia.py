import requests
from bs4 import BeautifulSoup
import time
import re
import xlwt
import threading
from operator import itemgetter, attrgetter
def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except ZeroDivisionError as e:
        raise ValueError(e)
def house_info(infolist,html):
    try:
        soup = BeautifulSoup(html,'html.parser')
        link_list = [i.attrs['href'] for i in soup.select('a.img')]
        title_list = [i.get_text() for i in soup.select('.info > .title')]
        houseinfo_list = [i.get_text().replace(u'\xa0', u' ') for i in soup.select('.address > .houseInfo')]
        dealDate_list = [i.get_text() for i in soup.select('.address > .dealDate')]
        totalPrice_list = [float(i.get_text()) for i in soup.select('.address > .totalPrice > .number')]
        years_list = [re.findall(r'\d{4}',i.get_text())for i in soup.select('.flood > .positionInfo')]
        unitPrice_list = [i.get_text() for i in soup.select('.unitPrice > .number')]
        dealCycleTxt_list = [i.get_text() for i in soup.select('.dealCycleeInfo > .dealCycleTxt')]
        for n in range(len(link_list)):
            link,title,house_info,dealDate = link_list[n],title_list[n],houseinfo_list[n],dealDate_list[n]
            totalPrice, years, unitPrice, dealCycleTxt = totalPrice_list[n], years_list[n],unitPrice_list[n],dealCycleTxt_list[n]
            infolist.append([link,title,house_info,dealDate,totalPrice,years,unitPrice,dealCycleTxt])
    except ZeroDivisionError as e:
        raise ValueError(e)
def plist(infolist):
    infolist = sorted(infolist,key=lambda infolist : infolist[4],reverse=False)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('cdlianjia')
    ws.write(0, 0, '房屋链接')
    ws.write(0, 1, '房屋标题')
    ws.write(0, 2, '房屋朝向')
    ws.write(0, 3, '成交时间')
    ws.write(0, 4, '总价（万）')
    ws.write(0, 5, '单价（元/平）')
    ws.write(0, 6, '建筑时间')
    ws.write(0, 7, '其他')
    p = 1
    for e in range(len(infolist)):
        try:
            ws.write(p, 0, infolist[e][0])
            ws.write(p, 1, infolist[e][1])
            ws.write(p, 2, infolist[e][2])
            ws.write(p, 3, infolist[e][3])
            ws.write(p, 4, infolist[e][4])
            ws.write(p, 5, infolist[e][6])
            ws.write(p, 6, infolist[e][5])
            ws.write(p, 7, infolist[e][7])
            p+=1
            wb.save('I://cdlianjia.xls')
        except ZeroDivisionError as e:
            raise ValueError(e)
def main(depth_num):
    depth = depth_num
    infolist = []
    start_time = time.time()
    for l in range(depth):
        try:
            url = "https://cd.lianjia.com/chengjiao/pg" + str(l+1) + 'ng1nb1/'
            html = gethtml(url)
            house_info(infolist,html)
        except ZeroDivisionError as e:
            raise ValueError(e)
    plist(infolist)
    print("time", time.time() - start_time)
main(9)