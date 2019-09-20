import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

params = {
    'maintype': 'num',
    'uid': '5af303e3',
    'aids': '02ydm2',
    'requestId': 'aritlces_number_9270'
}

url = 'http://comet.blog.sina.com.cn/api'

response = requests.get(url, headers=headers, params=params)

print(response.text)
