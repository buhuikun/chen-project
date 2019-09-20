import json
import time
import pymysql
import requests
from bs4 import BeautifulSoup

# 蘑菇代理的隧道订单
appKey = "aEloVXhTYXFmZFJ2YWVkTTpOTTcyWG1id2lxeHduRmRI"

# 蘑菇隧道代理服务器地址
ip_port = 'secondtransfer.moguproxy.com:9001'

proxy = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
         "http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {"Proxy-Authorization": 'Basic ' + appKey}
base_url = 'https://book.douban.com'
def geturl(url):
    time.sleep(2)
    response = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    html = response.text
    s = requests.session()
    s.keep_alive = False
    return BeautifulSoup(html, 'lxml')


def getdouban(url):
    soup = geturl(url)
    tables = soup.select('.tagCol')
    for table in tables:
        alist = table.select('td > a')
        for a in alist:
            getTag(base_url+a.attrs['href'])


def save(book):
    conn = pymysql.connect('127.0.0.1', port=3306, db='db_spider', user='root', password='root')
    cur = conn.cursor()
    sql = 'insert into t_douban values (0, %s, %s, %s, %s, %s, %s)'
    cur.execute(sql, book)
    conn.commit()
    cur.close()
    conn.close()
    print('插入数据库','  ',book[0])

def getTag(url):
    soup = geturl(url)
    lilist = soup.select('.subject-item')

    for li in lilist:
        try:
            book = []
            img = li.select_one('.pic > a > img').attrs['src']
            title = li.select_one('.info > h2 >a').get_text()
            pub = li.select_one('.info > .pub').get_text()
            rating = li.select_one('.info > .star > .rating_nums').get_text()
            pl = li.select_one('.info > .star > .pl').get_text()
            p = li.select_one('.info > p').get_text()
            book.append(title)
            book.append(img)
            book.append(pub)
            book.append(rating)
            book.append(pl)
            book.append(p)
            save(book)
        except Exception as e:
            print(e)
    next = soup.select_one('.next > a')
    if next:
        getTag(base_url+next.attrs['href'])



if __name__ == '__main__':
    url = 'https://book.douban.com/tag/?icn=index-nav'
    getdouban(url)