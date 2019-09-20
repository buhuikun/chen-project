import time

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
}


def geturl(url):
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    return soup

# 获取所有相册
def getxiangce(soup):
    li = soup.select('.ml.mla.cl > li >div > a')
    return li

# 获取单个相册
def getimg(soup):
    alist = soup.select('.ptw.ml.mlp.cl > li > a')
    return alist

# 下载
def down(url):
    response = requests.get(url, headers=headers)
    return response.content

# 获取图片
def downimg(soup):
    src = soup.select_one('#pic').attrs['src']
    return src

def next(soup):
    return soup.select_one('.nxt').attrs['href']

if __name__ == '__main__':
    url = 'http://www.kongjie.com/home.php?mod=space&do=album&view=all&page=20'
    page = 1
    a = 0
    while True:
        print('获取第' + str(page) + '页相册')
        page += 1
        soup = geturl(url)
        # 获取下一页url
        url = next(soup)
        urllist = getxiangce(soup)

        for u in urllist:
            soup = geturl(u.attrs['href'])
            alist = getimg(soup)
            if alist:
                for i in alist:
                    soup = geturl(i.attrs['href'])
                    src = downimg(soup)
                    with open('image/'+str(time.time())+'.jpg', 'bw') as f:
                        f.write(down(src))
                    a += 1
                    print('成功下载'+str(a)+'张图片')

