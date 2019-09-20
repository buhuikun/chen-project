import requests
from bs4 import BeautifulSoup
import pymongo

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}


def geturl(url):
    response = requests.get(url, headers)
    html = response.text
    return BeautifulSoup(html, 'lxml')


def gettype(url):
    soup = geturl(url)
    alist = soup.select('a.f12')
    for a in alist:
        title = a.get_text()
        soup = getlist(url+a.attrs['href'])


def getlist(url):
    soup = geturl(url)
    liList = soup.select('div.list > ul > li')
    for li in liList:
        href = li.select_one('h3 > span > a').attrs['href']
        soup = geturl(href)
        getcontent(soup)


def save():
    server = 'localhost'
    port = '27017'
    dbname = 'admin'
    user = ''
    pwd = ''
    uri = 'mongodb://'+server+':'+port+'/'+dbname
    client = pymongo.MongoClient(uri)
    db = client['db_spider']
    collec_ylqx = db['collec_ylqx']
    return collec_ylqx



def getcontent(soup):
    text01li = soup.select('.text01 > ul > li')
    name = text01li[0].select_one('h3').get_text()
    category = text01li[1].contents[1].string.strip()
    enname = text01li[2].select_one('h3').get_text()
    pzwh = text01li[3].select_one('h3').get_text()
    zygg = text01li[4].get_text()
    text03 = soup.select_one('.text03').get_text()
    imgsrc = soup.select_one('.img > a > img').attrs['src']
    text04li = soup.select('.text04 > ul > li')
    scqy = text04li[1].get_text()
    lxr = text04li[2].get_text()
    lxdh = text04li[3].get_text()
    phone = text04li[4].get_text()
    lxcz = text04li[5].get_text()
    email = text04li[6].get_text()
    gswz = text04li[7].get_text()
    dwdz = text04li[8].get_text()
    yzbm = text04li[9].get_text()
    ylqx = {}
    ylqx['text03'] = text03
    ylqx['imgsrc'] = imgsrc
    ylqx['name'] = name
    ylqx['category'] = category
    ylqx['enname'] = enname
    ylqx['pzwh'] = pzwh
    ylqx['zygg'] = zygg
    ylqx['scqy'] = scqy
    ylqx['lxr'] = lxr
    ylqx['lxdh'] = lxdh
    ylqx['phone'] = phone
    ylqx['lxcz'] = lxcz
    ylqx['email'] = email
    ylqx['gswz'] = gswz
    ylqx['dwdz'] = dwdz
    ylqx['yzbm'] = yzbm
    collec_ylqx = save()
    collec_ylqx.insert(ylqx)
    print('保存成功：'+name)





if __name__ == '__main__':
    url = 'http://www.chinamedevice.cn/'
    gettype(url)

