# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from lianjiaspider.items import LianjiaspiderItem


class Lianjia2Spider(RedisSpider):
    name = 'lianjia2'
    redis_key = 'lianjia2:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(Lianjia2Spider, self).__init__(*args, **kwargs)

    url = 'https://sh.lianjia.com/ershoufang/'
    page = 1

    def parse(self, response):
        # print(response.text)
        alist = response.xpath('//a[@class="noresultRecommend img LOGCLICKDATA"]/@href')
        for a in alist:
            # print(a.extract())
            yield scrapy.Request(a.extract(), callback=self.parse_item)

        if self.page <= 100:
            self.page += 1
            yield scrapy.Request(self.url + 'pg' + str(self.page), callback=self.parse)

    def parse_item(self, response):
        title = response.xpath('//h1[@class="main"]/text()')[0].extract().strip()
        print('title：', title)
        total = response.xpath('//span[@class="total"]/text()')[0].extract().strip()
        print('total：', total)
        price = response.xpath('//span[@class="unitPriceValue"]/text()')[0].extract().strip()
        print('price:', price)
        area = response.xpath('//div[@class="houseInfo"]/div[@class="area"]/div[@class="mainInfo"]/text()[last()]')[
            0].extract().strip()
        print('area:', area)
        hx = response.xpath('//div[@class="mainInfo"]/text()[1]')[0].extract().strip()
        print('hx:', hx)
        number = response.xpath('//div[@class="houseRecord"]/span[@class="info"]/text()')[0].extract().strip()
        print('number:', number)
        item = LianjiaspiderItem()
        item['title'] = title
        item['total'] = total
        item['price'] = price
        item['area'] = area
        item['hx'] = hx
        item['number'] = number

        yield item
