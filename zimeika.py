# import requests
# import re
# def gethtml(url):
#     try:
#         headers = {
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#             'Accept-Encoding': 'gzip, deflate',
#             'Cookie': 's007df62c=tq52dpcnnhvts6holrg1b0na85; UM_distinctid=1611b6225cc13c-02d1f7f29ec5b7-3b3e5906-1fa400-1611b6225cd110; user_token_status=homNrX6jh2mzeabahoh4Z4Z9xZu9obaus7h7rIWHfWWIfIlpioB4nb95upeSeHmhkLO2rb2upms; CNZZDATA1261651588=884143683-1516577904-%7C1516577904; Hm_lvt_c501e68ec4f8d48b652a9d50c8401586=1516582874; Hm_lpvt_c501e68ec4f8d48b652a9d50c8401586=1516582944',
#             'Host': 'zimeika.com',
#             'Referer': 'http://zimeika.com/article/lists/tiantian.html',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
#         }
#         r = requests.get(url,headers=headers)
#         r.raise_for_status()
#         r.encoding = 'utf-8'
#         print(r.text)
#     except ZeroDivisionError as e:
#         raise ValueError(e)
# gethtml('http://zimeika.com/article/lists/tiantian.html?cate_id=1&time_type=&read_order=&type=&author_id=&author_name=&title=&p=1')
import pymysql
conn = pymysql.connect(host='211.149.173.153', port=3306, user='zhangmaode', passwd='zhang498660443',db='empirecms')
cur = conn.cursor()
cur.execute("SELECT * FROM phome_ecms_news")
for r in cur.fetchall():
    print(r)
#cur.close()
conn.close()