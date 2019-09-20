import json
import time

import requests
from lxml import etree


def geturl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
    }
    response = requests.get(url, headers=headers)
    html = response.text
    return etree.HTML(html)


def down(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'
    }
    response = requests.get(url, headers=headers)
    html = response.content
    s = requests.session()
    s.keep_alive = False

    return html

def getimg(xml):
    srclist = xml.xpath('//img[@class="BDE_Image"]/@src')
    # print(srclist)
    return srclist

def getdetail(xml):

    url = xml.xpath('//ul[@id="thread_list"]/li[contains(@class, "j_thread_list")]//a[@class="j_th_tit "]/@href')
    return url

if __name__ == '__main__':
    base_url = 'https://tieba.baidu.com'
    name = input('输入贴吧名字')
    stanum = int(input('输入开始页面'))
    endnum = int(input('输入结束页面'))
    for i in range(stanum, endnum+1):
        print('正在爬取第'+str(i)+'页数据...')
        url = 'https://tieba.baidu.com/f?kw='+name+'pn'+ str(i*50)
        # url = 'https://tieba.baidu.com/p/6203169775'
        # 获取列表页
        xml = geturl(url)
        # 获取列表url
        detail_url = getdetail(xml)
        # 获取详情页面
        a = 0
        for url in detail_url:
            detail = geturl(base_url+url)
            # # 获取详情页图片
            srclist = getimg(detail)
            for src in srclist:
                img = down(src)
                a += 1
                with open('image/'+name+'_'+str(time.time())+'.jpg', 'bw') as f:
                    f.write(img)
                    print('下载成功'+str(a)+'张图片...')

