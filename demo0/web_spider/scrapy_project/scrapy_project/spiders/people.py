# -*- coding: utf-8 -*-
import re

import scrapy


class PeopleSpider(scrapy.Spider):
    name = 'people'
    allowed_domains = ['people.com.cn']
    start_urls = ['http://politics.people.com.cn/GB/1024/index1.html']

    def __init__(self):
        self.page = 1
        self.max_page = 7
        self.str1 = 'http://politics.people.com.cn/GB/1024/index'
        self.str2 = '.html'

    def get_url(self):
        return self.str1 + str(self.page) + self.str2

    def parse(self, response):
        print(response.url)
        ul_list = response.xpath('//ul[contains(@class,"list_16 mt10")]')
        for ul in ul_list:

            for li in ul.xpath('.//li'):
                title = li.xpath('.//a/text()')[0].extract().strip()
                pub_date = li.xpath('.//em/text()')[0].extract().strip()
                print('title: ', title)
                print('pub_date: ', pub_date)

        p = self.str1 + r'(\d+)'
        cur_page = re.search(p, response.url).group(1)
        self.page = int(cur_page) + 1
        if self.page <= self.max_page:
            url = self.get_url()
            print('下一页')
            yield scrapy.Request(url, callback=self.parse)
