import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }

def down(url):
    response = requests.get(url, headers=headers)
    return response.text


def houselist(url):
    html = down(url)
    # print(html)
    pat1 = re.compile(r'<li class="clear LOGVIEWDATA LOGCLICKDATA.*?</li>', re.M | re.S)
    pat2 = re.compile(r'<div class="title">.*?<a.*?href="(.*?)".*?>(.*?)</a>', re.M | re.S)
    pat3 = re.compile(r'<span class="unitPriceValue">(.*?)<i>', re.M | re.S)
    pat4 = re.compile(r'<span class="total">(.*?)</span>', re.M | re.S)
    pat5 = re.compile(r'<div class="communityName">.*?<a.*?>(.*?)</a>', re.M | re.S)
    pat6 = re.compile(r'<div class="areaName">.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>.*?', re.M | re.S)
    pat7 = re.compile(r'<div class="visitTime">.*?<span class="info">(.*?)</span>', re.M | re.S)
    pat8 = re.compile(r'<div class="houseRecord">.*?<span class="info">(.*?)<span', re.M | re.S)
    pat9 = re.compile(r'<div class="base">.*?<ul>(.*?)</ul>', re.M | re.S)
    pat10 = re.compile(r'<li>.*?</li>', re.M | re.S)
    pat11 = re.compile(r'</span>(.*?)</li>', re.M | re.S)
    li = pat1.findall(html)
    for i in li:
        title = pat2.search(i).group(2)
        detailurl = pat2.search(i).group(1)
        house = down(detailurl)
        price = pat3.search(house).group(1)
        total = pat4.search(house).group(1)
        xqmc = pat5.search(house).group(1)

        area = pat6.search(house).group(1)+' '+pat6.search(house).group(2)
        visitTime = pat7.search(house).group(1)
        houseRecord = pat8.search(house).group(1)
        base = pat9.findall(house)[0]
        # print(base)
        baseli = pat10.findall(base)
        for li in baseli:
            hx = pat11.search(li).group(1)
            print(hx)
        print('='*40)


if __name__ == '__main__':
    url = 'https://sh.lianjia.com/ershoufang/rs/'
    houselist(url)



