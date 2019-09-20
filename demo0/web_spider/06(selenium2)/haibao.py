import time
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

temp = time.ctime().split(' ')
time_str = temp[1] + ' ' + temp[2] + ' ' + temp[4] + ' ' + temp[3] + 'GMT 0800 (中国标准时间)'


def geturl(url, skip):
    data = {
        'skip': skip,
    }
    params = {
        # 当前时间字符串
        'stampMon': time_str,
    }
    response = requests.post(url, headers=headers, params=params, data=data)
    # 返回response数据
    html = response.json()['result']['html']
    skip = response.json()['result']['skip']
    return html, skip


# 提取数据
def draw_data(res):
    pat = re.compile(r'originUrl="(.*?)">')
    url_list = pat.findall(res)
    for url in url_list:
        con = requests.get(url, headers=headers).content
        file_name = 'img/' + str(int(time.time() * 1000)) + '.jpg'
        with open(file_name, 'bw') as f:
            f.write(con)
        print(file_name, '下载成功...')


if __name__ == '__main__':
    url = 'http://pic.haibao.com/ajax/image:getHotImageList.json'
    skip = 76
    for i in range(1, 10):
        res, skip = geturl(url, skip)
        draw_data(res)

    print('=============' * 50)
