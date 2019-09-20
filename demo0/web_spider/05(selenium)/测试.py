from selenium import webdriver

browser = webdriver.PhantomJS()  # 无头浏览器
# browser = webdriver.Chrome()     # 谷歌浏览器
print(type(browser))

browser.get("http://www.baidu.com")  # 请求指定的网页
print(browser.page_source)  # 获取网页源码
browser.close()  # 关闭当前的标签页
# browser.quit()  #退出
