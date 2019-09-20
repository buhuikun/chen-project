import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
# driver = webdriver.PhantomJS()
kw = input('请输入：')
page = int(input('爬取的页数'))


def down(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.content


num = 0


def openChrome(url):
    global num
    driver.get(url)
    print('打开页面。。')
    time.sleep(2)

    inputkw = driver.find_element_by_id('kw')
    inputkw.clear()
    inputkw.send_keys(kw)
    print('输入：' + kw)
    time.sleep(1)
    # search = driver.find_element_by_class_name('s_search')
    clickjs = 'document.getElementsByClassName("s_search")[0].click()'
    driver.execute_script(clickjs)
    # search.click()
    print('点击搜索')

    time.sleep(2)
    # 获取当当前标签页的句柄
    cur_handle = driver.current_window_handle
    # print('当前窗口：',driver.current_window_handle)

    for i in range(page):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        print('页面滚动')
        time.sleep(1)

    hrefList = driver.find_elements_by_xpath('//div[@class="imgbox"]/a')
    for h in hrefList:
        href = h.get_attribute('href')
        js = 'window.open("%s")' % (href,)
        driver.execute_script(js)
        print('打开新页面')
        new_handle = ''
        # 获取当前所有标签页的列表
        all_handles = driver.window_handles
        # 遍历找到新标签页的句柄
        for i in all_handles:
            if cur_handle != i:
                new_handle = i
        # 切换的新标签页
        driver.switch_to.window(new_handle)
        # print(driver.page_source)
        # print('当前窗口：', driver.current_window_handle)
        imgSrc = driver.find_element_by_xpath('//div[@class="img-wrapper"]/img')
        # print(imgSrc)
        with open('image/' + kw + str(int(time.time())) + '.jpg', 'bw') as f:
            f.write(down(imgSrc.get_attribute('src')))
        num += 1
        print('成功下载' + kw + str(int(time.time())) + '.jpg')
        print('=' * 30 + '第' + str(num) + '张图片' + '=' * 30)
        driver.close()
        driver.switch_to.window(cur_handle)
        print('关闭当前标签页')
        time.sleep(1)


if __name__ == '__main__':
    url = 'https://image.baidu.com/'
    openChrome(url)
