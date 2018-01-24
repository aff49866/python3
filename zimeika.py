import requests
import re
import pymysql
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
# cur.execute("SELECT * FROM phome_ecms_news")
# for r in cur.fetchall():
#     print(r)
#cur.close()
def getTianTianHtml(url):
    try:
        headers = {
            'authority': 'kuaibao.qq.com',
            'cookie': 'pgv_pvi=3894466560; RK=SIUOA7A6Td; pac_uid=1_155220296; kb_h5_user_id=KBH5UserId_151245445549256; tvfe_boss_uuid=9111743a133a0174; pgv_pvid=14073895; o_cookie=155220296; pgv_si=s4167611392; _qpsvr_localtk=0.19427851323596435; ptisp=ctc; ptcz=5e93651808285adca548c3c84d1b674c33256a4f48a68d0df89bfaa3eb95c831; uin=o0155220296; skey=@KB2aLQS0T; pt2gguin=o0155220296',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except ZeroDivisionError as e:
        raise ValueError(e)
def getInfo(html):
    try:
        regTitle = re.compile(r"'title': '(.*?)'", re.S)
        regContent = re.compile(r'<div class="content-box">(.*?)</div>', re.S)
        contentTxt ={}
        contentTxt['title'] = regTitle.findall(html)
        contentTxt['content'] = regContent.findall(html)
        # contentStr = contentTxt['content']
        # contentTxt['content'] = re.sub(r'本文(.*?)原创','',str(contentStr))
        return contentTxt
        # title.append(reg.findall(html)[0])
        # if reg2.findall(html):
        #     imagesmore = reg2.findall(html)
        # elif reg2.findall(html):
        #     imagesmore = reg3.findall(html)
        # else:
        #     imagesmore = reg4.findall(html)
        # imageslist = sorted(set(imagesmore), key=imagesmore.index)
        # for i in imageslist:
        #     imageurl = "http://p1.pstatp.com/origin/" + is
        #     infolist.append(imageurl)
    except ZeroDivisionError as e:
        raise ValueError(e)
def connectdb():
    db = pymysql.connect(host='211.149.173.153', port=3306, user='zhangmaode', passwd='zhang498660443',db='empirecms', charset='utf8')
    return db
def insertdb(db,contentTxt):
    cursor = db.cursor()
    sql = """INSERT INTO phome_ecms_news (classid,title)
             VALUES ('1','contentTxt["title"]')"""
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        print('插入数据失败!')
        db.rollback()
def closedb(db):
    db.close()
def main():
    # 抓取html
    html = getTianTianHtml('https://kuaibao.qq.com/s/20180122A107UE00')
    contentTxt = getInfo(html)
    # 连接数据库，插入数据
    db = connectdb()
    insertdb(db,contentTxt)
    closedb(db)
if __name__ == '__main__':
    main()