import json
import time

import requests

import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

params = {
    'refer': 'feed',
    'direction': 'loadmore',
}


def geturl(url):
    response = requests.get(url, headers=headers)
    return response.text


def get_data(i):

    # for i in data['page']['discoverFeeds']:
    # for i in data:
    # 用户名
    uname = i['item_detail']['uname']
    print('uname：', uname)
    # 喜欢数量
    like_count = i['item_detail']['like_count']
    print('like_count：', like_count)
    # 头像链接
    avatar = i['item_detail']['avatar']
    print('avatar：', avatar)
    # 分享数量
    share_count = i['item_detail']['share_count']

    print('share_count：', share_count)
    reply_count = i['item_detail']['share_count']
    print('reply_count：', reply_count)
    # 获取封面图片
    multi = i['item_detail']['multi']
    img = []
    if len(multi):
        for p in multi:
            img.append(p['path'])
    print('img：', img)
    print('=' * 100)


if __name__ == '__main__':
    url = 'https://bcy.net/'
    json_url = 'https://bcy.net/apiv3/common/getFeeds?refer=feed&direction=loadmore'

    html = geturl(url)
    pat1 = re.compile('parse\((.*?)\);')
    js = pat1.search(html).group(1)
    data = json.loads(js)
    data = json.loads(data)
    for i in data['page']['discoverFeeds']:
        get_data(i)
    for j in range(10):
        time.sleep(1)
        res = requests.get(json_url, headers=headers)
        item_info = json.loads(res.text)['data']['item_info']

        for i in item_info:
            get_data(i)

