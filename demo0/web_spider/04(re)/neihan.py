import json

import requests
import re
import redis

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}


def down(url):
    response = requests.get(url, headers=headers)
    # print(response.apparent_encoding)
    return response.content.decode('utf-8', errors='ignore')


def save(data):
    r = redis.StrictRedis(host='localhost', port=6379)
    r.lpush('neihan', data)


def duanzilist(url):
    base_url = 'https://www.neihan-8.com'
    html = down(url)
    pat1 = re.compile(r'<div class="text-column-item box box-790">.*?<div class="view" >.*?</div>', re.M | re.S)
    pat2 = re.compile(r'<h3>.*?<a href="(.*?)".*?>(.*?)</a>', re.M | re.S)
    pat3 = re.compile(r'<div class="good" >(.*?)</div>', re.M | re.S)
    pat4 = re.compile(r'<div class="bad" >(.*?)</div>', re.M | re.S)
    pat5 = re.compile(r'<div id="con_all".*?</p>(.*?)<div', re.M | re.S)
    pat6 = re.compile(r'<div class="pagenav".*?…</a><a href="(.*?)" class="next">下一页</a>', re.M | re.S)
    next = base_url + pat6.search(html).group(1)
    div = pat1.findall(html)
    for d in div:
        try:
            title = pat2.search(d).group(2)
            detailurl = base_url + pat2.search(d).group(1)
            good = pat3.search(d).group(1)
            bad = pat4.search(d).group(1)

            detail = down(detailurl)

            content = pat5.search(detail).group(1)
            data = {'title': title, 'good': good, 'bad': bad, 'content': content}
            save(json.dumps(data))
            print('成功保存数据', data)
        except Exception as e:
            print(e)
    print('开始爬取下一页...........')
    return duanzilist(next)


if __name__ == '__main__':
    try:
        url = 'https://www.neihan-8.com/article/index.html'
        duanzilist(url)

    except Exception as e:
        print('error: ', e)
