import requests
import csv
import codecs

from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}


url = 'https://movie.douban.com/chart'
response = requests.get(url, headers=headers)

html = response.text
# print(html)
lxml = etree.HTML(html)
lis = lxml.xpath('//div[@class="pl2"]')

for li in lis:
    title = li.xpath('.//a/span/text()')[0]
    score = li.xpath('.//span[@class="rating_nums"]/text()')[0]
    with codecs.open('./douban.csv', 'a', encoding='utf-8') as f:
        wr = csv.writer(f)
        wr.writerow([title,score])



