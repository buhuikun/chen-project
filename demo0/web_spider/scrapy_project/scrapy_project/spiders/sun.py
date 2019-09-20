# -*- coding: utf-8 -*-
import re

import scrapy

from scrapy_project.scrapy_project.items import ScrapyProjectItem


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    page = 0
    def __init__(self):
        self.url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='

    def parse(self, response):
        print(response.url)
        tr_list = response.xpath('//table[@bgcolor="#FBFEFF"]//tr')
        # count = response.xpath('//div[@class="pagination"]//text()')[0].extract().strip()
        # print('aaaaaa', count)
        for tr in tr_list:
            num = tr.xpath('.//td[@width="53"]/text()')[0].extract().strip()
            print('编号：', num)
            title = tr.xpath('.//td[@width="590"]/a[@class="news14"]/text()')[0].extract().strip()
            print('标题：', title)
            href = tr.xpath('.//td[@width="590"]/a[@class="news14"]/@href')[0].extract().strip()
            print('链接：', href)
            peo = tr.xpath('.//td[@width="105"]/text()')[0].extract().strip()
            print('网友：', peo)
            pub_date = tr.xpath('.//td[@width="121"]/text()')[0].extract().strip()
            print('时间：', pub_date)
            print('=' * 100)
            # yield scrapy.Request(href, callback=self.get_content)
            item = ScrapyProjectItem()

        pat = re.compile('pagination.*?共(\d+)条记录')
        count =  pat.search(response.body.decode(response.encoding)).group(1)
        if self.page < int(count):
            self.page += 30
            print('下一页')
            url = self.url + str(self.page)
            yield scrapy.Request(url, callback=self.parse)

    def get_content(self, response):
        try:
            td = response.xpath('//div[@class="wzy1"]//td[@class="txt16_3"]')
            content = td[0].xpath('./text()')[0].extract().strip()
            print(response.url)
            # print('内容：', content)
            return content
        except Exception as e:
            print('error:', e)
            content = '无'
            return content
