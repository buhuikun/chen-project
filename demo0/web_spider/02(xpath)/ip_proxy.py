import requests

# 蘑菇代理的隧道订单
appKey = "T1BVYVVNe*******eTQ1Mmdq"

# 蘑菇隧道代理服务器地址
ip_port = 'secondtransfer.moguproxy.com:9001'

# 准备去爬的 URL 链接
url = 'https://ip.cn'

proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {"Proxy-Authorization": 'Basic ' + appKey}
r = requests.get("https://ip.cn", headers=headers, proxies=proxy, verify=False, allow_redirects=False)
print(r.status_code)
print(r.content)
if r.status_code == 302 or r.status_code == 301:
    loc = r.headers['Location']
    print(loc)
    url_f = loc
    r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    print(r.status_code)
    print(r.text)
