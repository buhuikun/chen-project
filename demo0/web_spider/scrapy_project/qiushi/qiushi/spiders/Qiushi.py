# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qiushi.items import QiushiItem


class QiushiSpider(CrawlSpider):
    name = 'Qiushi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/8hr/page/1/']
    pagelink = LinkExtractor(restrict_xpaths=('//ul[@class="pagination"]/li[last()]/a'))
    rules = [
        Rule(pagelink, callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        item = QiushiItem()
        li_list = response.xpath('//div[@class="recommend-article"]//li')
        for li in li_list:
            img = li.xpath('./a/img/@src')[0].extract().strip()
            print('img:', img)
            title = li.xpath('./div/a/text()')[0].extract().strip()
            print('title:', title)
            author = li.xpath('.//a[@class="recmd-user"]/span/text()')[0].extract().strip()
            print('author:', author)
            zannum = li.xpath('.//div[@class="recmd-num"]/span[1]/text()')[0].extract().strip()
            print('zan:', zannum)
            cumnum = li.xpath('.//div[@class="recmd-num"]/span[last()-1]/text()')[0].extract().strip()
            print('comment:', cumnum)
            print('==' * 100)
            item['title'] = title
            item['img'] = img
            item['author'] = author
            item['zannum'] = zannum
            item['cumnum'] = cumnum
            yield item

        print('=' * 50 + '下一页' + '=' * 50)
