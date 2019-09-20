import time

from selenium import webdriver

username = '18339255213'
password ='chenxinbo'

browser = webdriver.Chrome()

browser.maximize_window()
url = 'http:www.weibo.com/login.php'
browser.get(url)
time.sleep(2)
input_login = browser.find_element_by_id("loginname")
input_login.clear()
input_login.send_keys(username)
time.sleep(2)
input_pwd = browser.find_element_by_name("password")
input_pwd.clear()
input_pwd.send_keys(password)
time.sleep(3)
print('登陆....')
btn = browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
btn.click()

time.sleep(10)
cookie = browser.get_cookies()
print(cookie)


time.sleep(10)
browser.close()