import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


def open_url(url):
    response = requests.get(url, headers=headers)
    return response.text




if __name__ == '__main__':
    url = 'https://g.hongshu.com/content/93416/13901181.html'
    html = open_url(url)
    print(html)




