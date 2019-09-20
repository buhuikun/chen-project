
from selenium import webdriver
import pytesseract
from PIL import Image
import time
from chaojiying import Chaojiying
from io import BytesIO


EMAIL = 'xn2233796049@163.com'
PASSWORD = '123456'

CHAOJIYING_USERNAME = '2271992921'
CHAOJIYING_PASSWORD = '2271992921'
CHAOJIYING_SOFT_ID = '1bce712d583f72be3a40d5960a86c94f'
CHAOJIYING_KIND = 1004

browser = webdriver.Chrome()
url = 'http://my.cnki.net/elibregister/commonRegister.aspx'
browser.get(url)
#html = browser.page_source
#print(html)

user = browser.find_element_by_id('username')
pwd = browser.find_element_by_id('txtPassword')
email = browser.find_element_by_id('txtEmail')
checkCode = browser.find_element_by_id('txtOldCheckCode')
btnReg = browser.find_element_by_id('ButtonRegister')
user.send_keys('guojiantao3@163.com')
time.sleep(2)
pwd.send_keys('mimamima')
time.sleep(2)
email.send_keys('guojiantao3@163.com')
time.sleep(2)


browser.save_screenshot('./images/zhiwang.png')
img = browser.find_element_by_id('checkcode')
left = img.location['x']#验证码图片左上角横坐标
top = img.location['y']#验证码图片左上角纵坐标
right = left + img.size['width']#验证码图片右下角横坐标
bottom = top + img.size['height']#验证码图片右下角纵坐标
im=Image.open('./images/zhiwang.png')
im_crop=im.crop((left,top,right,bottom))#这个im_crop就是从整个页面截图中再截出来的验证码的图片
im_crop.save('./images/zrecaptchar.png')

chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)
# 识别验证码
bytes_array = BytesIO()
im_crop.save(bytes_array, format='PNG')
strcode = chaojiying.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND)
print(strcode)


checkCode.send_keys(strcode['pic_str'])

#模拟点击按钮
#btnReg.click()