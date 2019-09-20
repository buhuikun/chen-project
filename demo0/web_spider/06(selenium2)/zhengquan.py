import json

import requests
import re

def getcount(url):
    params = {

        'node': 'sh_a',

    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    response = requests.get(url, params=params, headers=headers)
    return response.text

def getconent(url, page, node):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    params = {
        'page': page,
        'num': '40',
        'sort': 'symbol',
        'asc': '1',
        'node': node,
        'symbol': '',
        '_s_r_a': 'init',
    }
    response = requests.get(url, params=params, headers=headers)
    return response.text

if __name__ == '__main__':
    url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData'
    countUrl = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount'
    nodes = ['sh_a', 'sh_b', 'sz_a', 'sz_b', 'sh_z', 'sz_z', 'hs_a', 'hs_b', 'hs_z', 'close_fund', 'hs_s', 'zxqy', 'hs_qz', 'cyb', 'shfxjs']
    countstr = getcount(countUrl)

    pat = re.compile('(\d+)')
    count = pat.search(countstr).group(1)
    print(count)
    for page in range(1, int(count)//40+2):
        for node in nodes:
            print(node)
            content =getconent(url, page, node)
            # 用正则表达式匹配{ }数据
            pat1 = re.compile(r'({.*?})')
            data = pat1.findall(content)
            for d in data:
                print(type(d), d)
        print('='*100)







