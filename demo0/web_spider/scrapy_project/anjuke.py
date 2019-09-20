import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


def geturl(url):
    response = requests.get(url, headers=headers)
    print(response.text)
    return etree.HTML(response.text)


def getdata(html):
    pass

    # lis = html.xpath('//li[@class="list-item"]')
    # for li in lis:
    #     title = li.xpath('.//div[@class="house-title"]/a/text()')[0].strip()
    #     print(title)


if __name__ == '__main__':
    url = 'http://www.dianping.com/zhengzhou/ch10/g117p2'
    html = geturl(url)
    getdata(html)
    # for i in range(1, 100):
    #     url = 'https://zhengzhou.anjuke.com/sale/sale/p{}/'.format(i)
    #     html = geturl(url)
    #     getdata(html)
    #     print(i, '=' * 100)
