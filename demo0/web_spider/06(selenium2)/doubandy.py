import requests
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


def getTag(url):
    params = {
        'type': 'movie',
        'source': ''
    }
    response = requests.get(url, params=params, headers=headers)
    return response.json()['tags']


def geturl(url, tag, page_start=0):
    params = {
        'type': 'movie',
        'tag': tag,
        'sort': 'recommend',
        'page_limit': 20,
        'page_start': page_start,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()['subjects']


if __name__ == '__main__':
    url = 'https://movie.douban.com/j/search_subjects'
    tag_url = 'https://movie.douban.com/j/search_tags?type=movie&source='
    tags = getTag(tag_url)
    for tag in tags:
        for i in range(10):
            response = geturl(url, tag, i * 20)
            print()
            for data in response:
                print('类型：', tag, '---', data)
