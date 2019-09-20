import random
import time

from selenium import webdriver
username = '18339255213'
password = 'chenxinbo'

def login():
    # 定义浏览器
    driver = webdriver.Chrome()
    try:
        # 窗口最大化
        driver.maximize_window()
        url = 'http://www.weibo.com/login.php'
        driver.get(url)
        time.sleep(2)
        print('输入用户名...')
        input_username = driver.find_element_by_id('loginname')
        # 清除输入框的内容
        input_username.clear()
        input_username.send_keys(username)
        time.sleep(1)
        print('输入密码')
        input_password = driver.find_element_by_name('password')
        input_password.clear()
        input_password.send_keys(password)
        time.sleep(2)
        print('点击登录...')
        btn = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
        btn.click()
        time.sleep(3)
        return driver

    except Exception as e:
        print('error: ', e)


def weibospider(driver):
    try:

        time.sleep(10)
        # 获取页面高度
        last_height = driver.execute_script('return document.body.scrollHeight;')
        print('滚动事件', last_height)
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            print('开始滚动')
            time.sleep(random.random()*10)
            new_height = driver.execute_script('return document.body.scrollHeight;')
            if new_height == last_height:
                print('停止滚动')
                break
            else:
                print('继续滚动')
                last_height = new_height
        print('提取数据...')
        ls = driver.find_elements_by_xpath('//div[@class="WB_detail"]')
        print('ls', len(ls))
        for item in ls:
            name = item.find_element_by_xpath('.//a[@class="W_f14 W_fb S_txt1"]').text
            print(name)
            pub_date = item.find_element_by_xpath('.//div[@class="WB_from S_txt2"]/a').text
            print(pub_date)
            content = item.find_elements_by_xpath('.//div[@class="WB_text W_f14"]')
            if len(content)>0:
                content = content[0].text.strip()
            else:
                content = 'none'


            print(content)
            print('='*50)
        time.sleep(5)
        next = driver.find_element_by_xpath('//a[@class="page next S_txt1 S_line1"]')
        next.click()
        print('下一页')
        weibospider(driver)


    except Exception as e:
        print('spider_error:', e)



if __name__ == '__main__':
    driver = login()
    url = 'https://weibo.com/p/1003061826792401?is_all=1'
    print('微博页面...')
    driver.maximize_window()
    driver.get(url)
    weibospider(driver)







