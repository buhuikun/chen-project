import time

from selenium import webdriver

driver = webdriver.PhantomJS()
# driver = webdriver.Chrome()
# driver.maximize_window()
# key = input('输入...')
key = '手机'

a = 0


def search():
    print('页面打开')
    # time.sleep(3)
    print('搜索' + key + '。。。')
    search = driver.find_element_by_id('key')
    search.clear()
    search.send_keys(key)
    btn = driver.find_element_by_class_name('button')
    btn.click()
    time.sleep(2)


page = 1


def openChrome():
    global a, page
    print(' ' * 30 + '第' + str(page) + '页' + ' ' * 30)
    i = 0
    height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        i += 1
        time.sleep(1)
        newHeight = driver.execute_script('return document.body.scrollHeight')
        if newHeight == height:
            print('结束滚动！')
            break
        else:
            height = newHeight
            print('向下滚动' + str(i + 1) + '次')
    print('提取数据...')

    li = driver.find_elements_by_xpath('//li[@class="gl-item"]')
    for i in li:
        title = i.find_element_by_xpath('.//div[@class="p-name p-name-type-2"]//em').text
        print('标题：', title)
        url = i.find_element_by_xpath('.//div[@class="p-name p-name-type-2"]/a').get_attribute('href')
        print('链接：', url)
        price = i.find_element_by_xpath('.//div[@class="p-price"]//i').text
        print('价格：', price)
        comment = i.find_element_by_xpath('.//div[@class="p-commit"]//a').text
        print('评论数：', comment)
        try:
            shop = i.find_element_by_xpath('.//div[@class="p-shop"]//a').text
            print('店铺：', shop)
        except Exception as e:
            shop = '未知'
            print('error: ', e)
        a += 1
        print('-' * 50 + str(a) + '-' * 50)
    try:
        next = driver.find_element_by_class_name('pn-next')
        next.click()
        time.sleep(5)
        page += 1
        openChrome()
    except Exception as e:
        print('netError：', e)


if __name__ == '__main__':
    url = 'https://www.jd.com/2019'
    driver.get(url)
    search()
    openChrome()
