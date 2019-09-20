import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

url = 'http://www.xietd.com/data/attachment/forum/201904/09/160342ayfmzmroum7gzmde.jpg'
response = requests.get(url, headers=headers)
print(response.status_code)
with open('images/a.jpg', 'bw')as f:
    f.write(response.content)
