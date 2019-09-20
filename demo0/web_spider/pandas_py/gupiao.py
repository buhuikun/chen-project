import requests
from lxml import etree
import csv
import codecs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


def open_url(url):
    response = requests.get(url, headers=headers)
    return etree.HTML(response.text)


def get_con(lxml):
    tabs = lxml.xpath('//table[@class="wsod_dataTable wsod_dataTableBig"]//tr')
    tabs.pop(0)
    for t in tabs:
        title = t.xpath('./td[@class="wsod_firstCol"]/a/text()')[0]
        company = t.xpath('./td[@class="wsod_firstCol"]/span/text()')[0]
        price = t.xpath('./td[@class="wsod_aRight"][1]/span/text()')[0]
        change1 = t.xpath('./td[@class="wsod_aRight"][2]/span/span/text()')[0]
        change2 = t.xpath('./td[@class="wsod_aRight"][3]/span/span/text()')[0]
        volume = t.xpath('./td[@class="wsod_aRight"][4]/text()')[0]
        change3 = t.xpath('./td[@class="wsod_aRight"][5]/span/text()')[0]
        with codecs.open('gupiao.csv', 'a', encoding='utf-8')as f:
            wr = csv.writer(f)
            wr.writerow([title, company, price, change1, change2, volume, change3])
        print(title, '--', company, '--', price, '--', change1, '--', change2, '--', volume, '--', change3)


if __name__ == '__main__':
    url = 'https://money.cnn.com/data/dow30/'
    lxml = open_url(url)
    get_con(lxml)
