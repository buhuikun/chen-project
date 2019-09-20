import json

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
}

url = 'http://www.4399.com/?haoqqdh'
response = requests.get(url, headers=headers)

html = response.content.decode('gb2312')
xml = etree.HTML(html)

# 手游
shouyou = xml.xpath('//a[@class="for_phone"]')[0]
for_phone = xml.xpath('//a[@class="for_phone"]/text()')
mi_ul = shouyou.xpath('../ul[@class="mi_ul"]/li/a/text()')
temp = {
    'category': for_phone[0],
    'content': mi_ul,
}
with open('4399.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(temp, ensure_ascii=False) + '\n')

# 前八个分类
mi_d = xml.xpath('//div[@class="mi-lr"]')
for cate in mi_d:
    category = cate.xpath('.//a[@class="mi_tit"]/text()')
    con = cate.xpath('.//div[@class="mi_d"]/span/a/text()')
    temp = {
        'categroy': category[0],
        'content': con,
    }
    with open('4399.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(temp, ensure_ascii=False) + '\n')

# 后四个分类
mi_g = xml.xpath('//div[@class="mi_g"]')
for m in mi_g:
    category = m.xpath('../a[last()]/text()')[0]
    con = m.xpath('.//a/text()')
    temp = {
        'category': category,
        'content': con,
    }
    with open('4399.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(temp, ensure_ascii=False) + '\n')


# 游戏分类
base_url = 'http://www.4399.com'
gamelist = xml.xpath('//ul[contains(@class, "tm_list")]')[:4]
for list in gamelist:
    category = list.xpath('..//div[@class="tm_tit"]/a/text()')[0]
    for game in list:
        name = game.xpath('.//a/text()')[0]
        url = base_url + game.xpath('.//a/@href')[0]
        temp = {
            'category': category,
            'name': name,
            'url': url,
        }
        with open('4399.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(temp, ensure_ascii=False) + '\n')
