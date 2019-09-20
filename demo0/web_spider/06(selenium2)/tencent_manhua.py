import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


def geturl(url, page=1):
    params = {
        'cid': 146,
        'token': '49cbb2154853ef1a74ff4e53723372ce',
        'ext': 'comic',
        'page': page,
        'expIds': '',
        'callback': '__jp4',
    }
    response = requests.get(url, headers=headers, params=params)
    return response.text


def draw_data(res):
    pat1 = re.compile(r'<script>window.chData=(.*?)</script>')
    pat2 = re.compile(r'({"app_id":.*?{"app_id":)')
    pat3 = re.compile(r'"title":"(.*?)",')
    pat4 = re.compile(r'"intro":"(.*?)",')
    pat5 = re.compile(r'multi_imgs":\["(http.*?)"\],')
    js = pat1.search(res).group(1)
    ls = pat2.findall(js)
    for item in ls:
        title = pat3.search(item).group(1)
        print(title)
        intro = pat4.search(item).group(1)
        print(intro)
        img = pat5.findall(item)
        print(img)


if __name__ == '__main__':
    url = 'https://new.qq.com/ch/comic/'
    # for i in range(10):
    res = geturl(url)
    draw_data(res)
