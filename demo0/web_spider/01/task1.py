import random
import time
from lxml import etree

import requests
statepage = int(input('开始页码'))
endpage = int(input('结束页码'))
kw = input('关键字')

headers = {
    # 'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}
# response = requests.get('https://tieba.baidu.com/f?kw=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80', headers=headers)
# print(response.text)
# print(response.content)

url = 'https://tieba.baidu.com/f?'

for page in range(statepage, endpage+1):
    pn = (page-1)*50

    params = {
        'kw': kw,
        'pn': pn,
    }
    response = requests.get(url,headers=headers,  params=params)
    print(response.encoding)
    print(response.apparent_encoding)
    print(response.text)
    time.sleep(random.random())
