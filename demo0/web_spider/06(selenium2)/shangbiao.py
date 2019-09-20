import json
import re

import requests


def getcontent(url, page=1):
    data = {
        'page': page,
        'rows': '20',
        'annNum': '1654',
        'annType': '',
        'tmType': '',
        'coowner': '',
        'recUserName': '',
        'allowUserName': '',
        'byAllowUserName': '',
        'appId': '',
        'appIdZhiquan': '',
        'bfchangedAgengedName': '',
        'changeLastName': '',
        'transferUserName': '',
        'acceptUserName': '',
        'regName': '',
        'tmName': '',
        'intCls': '',
        'fileType': '',
        'totalYOrN': 'false',
        'appDateBegin': '',
        'appDateEnd': '',
        'agentName': '',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    response = requests.post(url, data=data, headers=headers)
    return response.text


if __name__ == '__main__':
    url = 'http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearchDG.html'
    count = json.loads(getcontent(url))['total']//20+2
    for i in range(1, count):
        print('第',i, '页')
        res = json.loads(getcontent(url))
        response = res['rows']
        for data in response:
            print(data)