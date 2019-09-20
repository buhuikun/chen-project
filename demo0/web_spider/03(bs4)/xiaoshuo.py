import requests
from bs4 import BeautifulSoup

def geturl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    html = response.content.decode('GBK', errors='ignore')
    soup = BeautifulSoup(html, 'lxml')
    return soup

def geturllist(soup):
    base_url = 'https://www.quanben.net'
    detaillist = []
    chapterlist = soup.select('.chapterlist > dd > a')
    for i in range(10):
        chapterlist.pop(0)
    for chap in chapterlist:
        detaillist.append(base_url+chap.attrs['href'])
    return detaillist


def getcontent(soup):
    BookCon = soup.select('#BookCon')[0]
    title = BookCon.select('h1')[0].string
    content = BookCon.select('#BookText')[0].get_text()
    return title, content

if __name__ == '__main__':

    url = 'https://www.quanben.net/4/4408/'
    soup = geturl(url)
    name = soup.select_one('.btitle > h1').get_text()
    # 获取章节url
    urllist = geturllist(soup)
    # 遍历每一个章节
    for detailurl in urllist:
        detail = geturl(detailurl)
        title, content = getcontent(detail)
        with open(name+'.txt', 'a', encoding='utf-8') as f:
            f.write('\n'+title+'\n\n'+content+'\n')
            print('成功下载'+title)
