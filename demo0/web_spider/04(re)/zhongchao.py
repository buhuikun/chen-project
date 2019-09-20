import json

import requests
import re
import redis

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}


def down(url):
    response = requests.get(url, headers=headers)
    return response.text


def save(data):
    r = redis.StrictRedis(host='localhost', port=6379)
    r.lpush('zhongchao', data)


def getdate(url):
    html = down(url)
    pat1 = re.compile(r'(<div class="news_item">.*?<div class="share">.*?</ul>)', re.M | re.S)
    pat2 = re.compile(r'<h3>.*?<a.*?href="(.*?)">(.*?)</a></h3>', re.M | re.S)
    pat3 = re.compile(r'<div class="keywords">.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>', re.M | re.S)
    pat4 = re.compile(r'<div class="share_join">.*?<span class="icon">(\d+)</span>', re.M | re.S)
    ls = pat1.findall(html)
    for item in ls:
        title_obj = pat2.search(item)
        if title_obj:
            title = title_obj.group(2)

        url_obj = pat2.search(item)
        if url_obj:
            url = url_obj.group(1)

        tag_obj = pat3.search(item)
        if tag_obj:
            tag = tag_obj.group(1) + '-' + tag_obj.group(2)

        comment_obj = pat4.search(item)
        if comment_obj:
            comment = comment_obj.group(1)
        data = {'title': title, 'url': url, 'tag': tag, 'comment': comment}
        save(json.dumps(data))
        print('成功保存数据：', data)


if __name__ == '__main__':
    try:
        for page in range(1, 2):
            if page == 1:
                url = 'http://sports.163.com/zc/'
            else:
                if page < 10:
                    page_str = '0' + str(page)
                else:
                    page_str = str(page)
                url = 'https://sports.163.com/special/00051C89/zc_' + page_str + '.html'
            getdate(url)

    except Exception as e:
        print('error: ', e)
