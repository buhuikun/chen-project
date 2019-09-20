import requests


import requests
import json

headers = {
    'User-Agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; MI 6  Build/NMF26X)'
}


url = 'http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=A7BB159A114D5C74A7DFEB2813A6FAE1&ovr=4.4.2&device=Xiaomi+_MI+6+&net_type=1&client_id=tmi%2BYROccsYYAiz9aIsg3g%3D%3D&info_ms=0w8gGn9%2Bri61LLoGkjOhyQ%3D%3D&info_ma=RidXlCsZC3qdH02P6d5SvyFWB4G42tuunG27HwCwv8g%3D&mno=0&info_la=1VB12UAn6DYfWP8Kr3j1jw%3D%3D&info_ci=1VB12UAn6DYfWP8Kr3j1jw%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=RidXlCsZC3qdH02P6d5SvyFWB4G42tuunG27HwCwv8g%3D&os_level=19&os_id=e4115b6091ef7012&resolution=720_1280&dpi=240&client_ip=192.168.13.179&pdunid=b6091ef7012e4115'


response = requests.get(url, headers=headers)
items = json.loads(response.text)['list']
# print(items)
i=1
for item in items:


    print(i ,item)
    i+=1
print('='*100)





