import json
import random
import time
import pymysql
import requests
from lxml import etree


# 对url发起请求，返回xml页面
def geturl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
    }

    response = requests.get(url, headers=headers)
    html = response.text
    return etree.HTML(html)


# 获取房源详情页面数据
def getcontent(xmls):
    house = []

    # 标题

    title = xmls.xpath('//div[@class="title-wrapper"]/div/div/h1[@class="main"]/text()')[0]
    classcontent = xmls.xpath('//div[@class="overview"]/div[@class="content"]')[0]
    # 单价和总价
    price = classcontent.xpath('.//div[@class="price "]/div/div/span[@class="unitPriceValue"]/text()')[0]
    total = classcontent.xpath('.//div[@class="price "]/span[@class="total"]/text()')[0]
    house.append(title)
    house.append(price)
    house.append(total)


    # 价钱信息
    classaroundInfo = classcontent.xpath('.//div[@class="aroundInfo"]/div')
    for item in classaroundInfo:
        label = item.xpath('.//span[@class="label"]/text()')[0]
        infos = item.xpath('.//a[@class="info "]//text() | .//span[@class="info"]//text()')
        # infos是一个列表，需要把每一项链接起来
        s = ''
        info = s.join(infos)
        house.append(info)


    # 基本信息
    introcontent = xmls.xpath('//div[@class="introContent"]')
    for base in introcontent:
        name = base.xpath('.//div[@class="base"]/div[@class="name"]/text()')[0]
        items = base.xpath('.//div[@class="base"]//li')
        for i in items:
            info = i.xpath('./text()')[0]
            label = i.xpath('./span/text()')[0]
            house.append(info)
        if len(items) < 12:
            for i in range(12-len(items)):
                house.append('暂无数据')

    # 基本属性
    for transaction in introcontent:
        name = transaction.xpath('.//div[@class="transaction"]/div[@class="name"]/text()')[0]
        items = transaction.xpath('.//div[@class="transaction"]//li')
        for i in items:
            label = i.xpath('./span/text()')[0]
            info = i.xpath('./span[last()]/text()')[0]
            house.append(info)
            if len(items) < 8:
                for i in range(8 - len(items)):
                    house.append('暂无数据')

    # # 房源特色
    # newwrap = xmls.xpath('//div[@class="newwrap baseinform"]/div/div[@class="baseattribute clear"]')
    # for wrap in newwrap:
    #     name = wrap.xpath('.//div[@class="name"]/text()')[0]
    #
    #     content = wrap.xpath('.//div[@class="content"]/text()')[0]
    #     house.append(content)
    return house

if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1', port=3306, db='db_lianjia', user='root', password='root')
    cur = conn.cursor()
    # 循环十页
    a = 0
    for pg in range(10):
        url = 'https://sh.lianjia.com/ershoufang/' + 'pg' + str(pg + 1)
        # 获取每一页房源
        xmls = geturl(url)
        lilist = xmls.xpath('//ul[@class="sellListContent"]/li[contains(@class,"clear")]/a/@href')
        # 遍历每一个房源的url，获取详情页
        for liurl in lilist:
            # 房源详情页面
            xmls = geturl(liurl)
            # 匹配每一个房源信息
            house = getcontent(xmls)
            print(len(house), '     ',house)
            a += 1
            sql = 'insert into lianjia values (0, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cur.execute(sql, house)
            conn.commit()
    cur.close()
    conn.close()

