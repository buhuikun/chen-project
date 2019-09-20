import random
import time

import requests
from lxml import etree
import pymysql


def geturl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    response = requests.get(url, headers)
    html = response.text
    # print(html)
    return etree.HTML(html)


def save(article):
    # 创建数据库链接
    conn = pymysql.connect(host='127.0.0.1', port=3306, db='db_spider', user='root', password='root')
    cur = conn.cursor()
    sql = 'insert into t_zhiwang values (0, %s, %s, %s, %s, %s, %s)'
    cur.execute(sql, article)
    conn.commit()

    # 关闭链接
    cur.close()
    conn.close()


def getarticle(xml):
    div = xml.xpath('//div[@class="mdui-col-xs-12 mdui-col-md-9 mdui-typo"]')
    for d in div:
        title = d.xpath('.//h3//text()')
        s = ''
        title = s.join(title)
        try:
            span = d.xpath('.//span//text()')
            author = span[0]
            qikan = span[1]
            ptime = span[2]
            type = span[3]
            p = d.xpath('.//p//text()')
            p = s.join(p)
            article = [title, author, qikan, ptime, type, p]
            # print(article)
            save(article)
        except Exception as e:
            print(title)
            print(e)


if __name__ == '__main__':

    word = input('输入要查找的文章...')
    page = int(input('输入要爬取的页数...'))
    for p in range(1, page + 1):
        print('正在爬取第' + str(p) + '页内容...')
        url = 'https://search.cn-ki.net/search?keyword='+word+'&p=' + str(p)
        xml = geturl(url)
        article = getarticle(xml)
