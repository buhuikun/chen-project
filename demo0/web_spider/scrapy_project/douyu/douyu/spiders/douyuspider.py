# -*- coding: utf-8 -*-
import json
from douyu.items import DouyuItem
import scrapy


class DouyuspiderSpider(scrapy.Spider):
    name = 'douyuspider'
    allowed_domains = ['douyucdn.cn']

    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [url]

    def parse(self, response):
        data = json.loads(response.text)['data']
        for each in data:
            item = DouyuItem()
            item['name'] = each['nickname']
            item['image_url'] = each['vertical_src']
            yield item
        # 翻页
        if self.offset <= 100:
            self.offset+=20
            yield scrapy.Request(self.url+str(self.offset), callback=self.parse)
