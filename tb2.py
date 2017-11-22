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

# import random
# def totle(totle):
#     a = random.randint(1000,5000)
#     b = totle - a
#     print(totle,a,b)
# totle(5000)

import random
# def constrained_sum_sample_pos(n, total):
# """Return a randomly chosen list of n positive integers summing to total.
#  Each such list is equally likely to occur."""
#  dividers = sorted(random.sample(xrange(1, total), n - 1))
#  return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
def constrained_sum_sample_pos(n, total):
    '''随机生成N个数，它们之和等于M。先随机生成N-1个数的列表list，从小到大排序，然后加入最小数0产生list2，加入最大数M产生list3，然后将列表中对应的项相减。生成最终的列表。 举例：随机产生[1,2,3,4]
那么如果最终之和是10，[1,2,3,4,10]减去[0,1,2,3,4]，得到新的列表[1,1,1,1,6]，然后各个数相加就等同于(1-0)+(2-1)+(3-2)+(4-3)+(10-4)=(1+2+3+4+10)-1-2-3-4-0=10-0=10，中间随机产生的数都抵销掉
然后可限定最终列表的最小值min(list)
'''
    dividers = sorted(random.sample(range(0,total,20), n - 1))
    num_list=[]
    for a, b in zip(dividers + [total], [0] + dividers):
        num_list.append(a-b)
    return num_list
list2 = constrained_sum_sample_pos(10, 29000)
while min(list2)<160:
    list2 = constrained_sum_sample_pos(10, 29000)
print(list2)