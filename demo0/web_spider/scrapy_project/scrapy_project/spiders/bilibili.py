# -*- coding: utf-8 -*-
import scrapy


class BilibiliSpider(scrapy.Spider):

    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking#!/all/0/0/7/']

    def parse(self, response):
        print(response.url)
        rank_item = response.xpath('//ul[@class="rank-list"]/li[@class="rank-item"]')
        print(len(rank_item))
        print('rank_item', rank_item)
        for each in rank_item:
            rank = each.xpath('.//div[@class="num"]/text()')[0].extract().strip()
            print(rank)
            name = each.xpath('.//a[@class="title"]/text()')[0].extract().strip()
            print(name)
            view = each.xpath('.//div[@class="detail"]/span[@class="data-box"]')
            print(len(view))


