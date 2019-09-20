import re
import json
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Referer': 'http://www.sse.com.cn/assortment/stock/list/share/'
}

url = 'http://query.sse.com.cn/security/stock/getStockListData.do?&jsonCallBack=jsonpCallback49389&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=2&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=1&_=1564386829581'
response = requests.get(url, headers=headers)
print(type(response.text))
print(response.text)

pat = re.compile(r'jsonpCallback\d+\((.*?)\)')
data = pat.search(response.text).group(1)
print(type(data))
data = json.loads(data)
print(data)