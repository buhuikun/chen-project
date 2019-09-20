import json
import random
import time
from lxml import etree
import requests

statepage = int(input('开始页码'))
endpage = int(input('结束页码'))
kw = input('关键字')

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
}

url = 'https://tieba.baidu.com/f?'

for page in range(statepage, endpage + 1):
    pn = (page - 1) * 50
    # get请求参数
    params = {
        'kw': kw,
        'pn': pn,
    }
    response = requests.get(url, headers=headers, params=params)
    html = response.text
    selector = etree.HTML(html)
    li = selector.xpath('//li[contains(@class," j_thread_list clearfix")]')
    print('li', len(li))
    base_url = 'https://tieba.baidu.com'
    # 匹配数据
    for item in li:
        title = item.xpath('.//a[@class="j_th_tit "]/text()')[0]
        detail_url = base_url + item.xpath('.//a[@class="j_th_tit "]/@href')[0]
        author = item.xpath('.//span[@class="frs-author-name-wrap"]/a/text()')[0]
        num = item.xpath('.//span[@class="threadlist_rep_num center_text"]/text()')[0]
        result = {
            'title': title,
            'detail_url': detail_url,
            'author': author,
            'num': num
        }
        print('title', title)
        with open('tieba.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(result, ensure_ascii=False) + '\n')
    # 延时爬取，防止点击过快
    time.sleep(random.random())
