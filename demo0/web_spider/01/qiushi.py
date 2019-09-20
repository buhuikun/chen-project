import json

import requests
from lxml import etree

url = 'https://www.qiushibaike.com/8hr/page/1/'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}

response = requests.get(url, headers=headers)
html = response.text

xml = etree.HTML(html)

items = xml.xpath('//div[@class="recommend-article"]/ul/li')
for item in items:
    title = item.xpath('.//div[@class="recmd-right"]/a/text()')[0]
    num = item.xpath('.//div[@class="recmd-num"]/span/text()')[0]
    comment = item.xpath('.//div[@class="recmd-num"]/span[last()-1]/text()')
    username = item.xpath('.//a[@class="recmd-user"]/span/text()')[0]
    userimgurl = 'https:' + item.xpath('.//a[@class="recmd-user"]/img/@src')[0]
    temp = {
        'title': title,
        'num': num,
        'comment': comment,
        'username': username,
        'userimgurl': userimgurl,
    }
    with open('qiushi.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(temp, ensure_ascii=False) + '\n')
