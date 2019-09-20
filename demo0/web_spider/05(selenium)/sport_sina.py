import time

from selenium import webdriver
# driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
driver.maximize_window()


def openchrome(url):
    driver.get(url)
    a = 0
    for i in range(9):
        print('页面滚动！')
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')


    print('开始提取数据')
    ls = driver.find_elements_by_xpath('//h3[@class="ty-card-tt"]')
    print(len(ls))
    for i in ls:
        title = i.text
        a+=1
        print(a, '-----', title)
    # time.sleep(1)


if __name__ == '__main__':
    url = 'http://sports.sina.com.cn/'
    openchrome(url)
