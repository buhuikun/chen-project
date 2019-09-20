import json
import time

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}


def geturl(url):
    response = requests.get(url, headers)
    html = response.text
    return BeautifulSoup(html, 'lxml')

def save(cai):
    with open('双色球.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(cai, ensure_ascii=False)+'\n')

def getnbt(url):
    soup = geturl(url)
    trlist = soup.select('tbody > tr')
    for i in range(2):
        trlist.pop(0)
    for tr in trlist:
        red = tr.select('.redColor')
        redcolor = ''
        for r in red:
            redcolor += r.get_text() + ' '
        bluecolor = tr.select_one('.blueColor').get_text()
        td = tr.select('td')
        for i in range(len(td)):
            qh = td[0].get_text()
            date = td[1].get_text()
            ztze = td[9].get_text()
            onezs = td[10].get_text()
            onejj = td[11].get_text()
            twozs = td[12].get_text()
            twojj = td[13].get_text()
            jcgc = td[14].get_text()
        cai = {
            'qh':qh,
            'date': date,
            'redcolor': redcolor,
            'bluecolor': bluecolor,
            'ztze': ztze,
            'onezs': onezs,
            'onejj': onejj,
            'twozs': twozs,
            'twojj': twojj,
            'jcgc': jcgc

        }
        save(cai)




if __name__ == '__main__':
    url = 'http://zst.aicai.com/ssq/openInfo/'
    getnbt(url)






