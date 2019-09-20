import time

from selenium import webdriver

driver = webdriver.PhantomJS()


# driver = webdriver.Chrome()

# driver.maximize_window()


def dpSpider(url):
    driver.get(url)
    time.sleep(3)
    hotel = driver.find_elements_by_xpath('//li[@class="hotel-block"]')
    for h in hotel:
        title = h.find_element_by_xpath('.//a[@class="hotel-name-link"]').text
        print('标题：', title)
        price = h.find_element_by_xpath('.//div[@class="price"]//strong').text
        print('价格：', price)
        place = h.find_element_by_xpath('.//p[@class="place"]').text
        print('位置：', place)
        place = h.find_element_by_xpath('.//div[@class="item-rank-ctn"]//a').text
        print('评论数：', place)


if __name__ == '__main__':
    url = 'http://www.dianping.com/shanghai/hotel'
    dpSpider(url)
