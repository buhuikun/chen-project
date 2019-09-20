# -*- coding: utf-8 -*-
import scrapy


class YangtseSpider(scrapy.Spider):
    name = 'yangtse'
    allowed_domains = ['yangtse.com']
    start_urls = ['http://www.yangtse.com/app/internet/']

    def __init__(self):
        self.url = 'http://www.yangtse.com/app/internet/'
        self.str1 = 'index_'

    def parse(self, response):
        div_list = response.xpath('//div[@class="box"]')
        for div in div_list:
            href = div.xpath('.//div[@class="box-img"]/a/@href')[0].extract().strip()
            print('链接：', href)
            title = div.xpath('.//div[@class="box-text-title"]/a/text()')[0].extract().strip()
            print('标题：', title)
            img = div.xpath('.//div[@class="box-img"]/a/img/@src')[0].extract().strip()
            print('封面：', img)
            pub_date = div.xpath('.//div[@class="box-text-time"]/span/text()')[0].extract().strip()
            print('发布时间：', pub_date)
            content = div.xpath('.//div[@class="box-text-text"]/a/text()')[0].extract().strip()
            print('内容：', content)
        # count = response.xpath('//ul[@class="fenye"]/a[@title="Total record"]/b/text()')[0].extract().strip()
        # pages = int(count)//12+2
        # print('当前url：', response.url)
        for i in range(10):
            url = self.url + self.str1 + str(i) + '.html'
            yield scrapy.Request(url, callback=self.parse)
