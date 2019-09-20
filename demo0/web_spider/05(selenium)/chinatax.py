import time

from selenium import webdriver
# driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

driver.maximize_window()


def openChrome(url):
    driver.get(url)
    # time.sleep(2)
    ls = driver.find_elements_by_xpath('//div[@class="notice"]//ul[@class="info_list isnewimg"]//li')
    for li in ls:
        title = li.find_element_by_xpath('.//a').get_attribute('textContent')
        print(title)
        href = li.find_element_by_xpath('.//a').get_attribute('href')
        print(href)


if __name__ == '__main__':
    url = 'http://henan.chinatax.gov.cn/003/index.html?NVG=0&LM_ID=1'
    openChrome(url)
