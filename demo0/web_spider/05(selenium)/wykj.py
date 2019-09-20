import random
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

def openchrome(url):
    driver.get(url)
    time.sleep(5)
    height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == height:
            print('滚动结束。。')
            break
        else:
            print('继续滚动。。')
            height = new_height

    div = driver.find_elements_by_xpath('//div[@class="data_row news_article clearfix"]')
    for d in div:
        title = d.find_element_by_xpath('.//div[@class="news_title"]//a').text
        print(title)
        href = d.find_element_by_xpath('.//div[@class="news_title"]//a').get_attribute('href')
        print(href)

if __name__ == '__main__':
    url = 'https://tech.163.com/'
    openchrome(url)