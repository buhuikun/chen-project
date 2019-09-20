import json

import requests
import re
import redis

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}


def down(url):
    response = requests.get(url, headers=headers)
    return response.content.decode('GBK', errors='ignore')


def save(data):
    r = redis.StrictRedis(host='localhost', port=6379)
    r.lpush('jokeji', data)


def jokelist(url):
    base_url = 'http://www.jokeji.cn'
    html = down(url)
    pat1 = re.compile(r'<td width="650" align="left">(.*?)<td width="310" align="right">', re.M | re.S)
    pat2 = re.compile(r'<table width="646".*?</table>', re.M | re.S)
    pat3 = re.compile(r'<td width="408".*?<a href="(.*?)".*?>(.*?)</a>', re.M | re.S)
    pat4 = re.compile(r'<td width="124".*?:(.*?)</td>', re.M | re.S)
    pat5 = re.compile(r'<td width="96".*?class="date">(.*?)</span>', re.M | re.S)
    ls = pat1.findall(html)[0]
    tables = pat2.findall(ls)
    for item in tables:
        a = pat3.search(item)
        title = a.group(2)
        detail_url = base_url + a.group(1)
        num = pat4.search(item).group(1)
        date = pat5.search(item).group(1).split(' ')[-1]
        detail = down(detail_url)
        pat6 = re.compile(r'<span id="text110">(.*?)</span>', re.M | re.S)
        content = pat6.search(detail).group(1)
        data = {'title': title, 'num': num, 'date': date, 'content': content}
        save(json.dumps(data))
        print('保存数据：', data)


if __name__ == '__main__':
    try:
        for page in range(1, 5):
            url = 'http://www.jokeji.cn/hot.asp?me_page=' + str(page)
            jokelist(url)

    except Exception as e:
        print('error: ', e)
