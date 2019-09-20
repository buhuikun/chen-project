# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from quanben.items import QuanbenItem


class QuanbenspiderSpider(CrawlSpider):
    name = 'quanbenspider'
    allowed_domains = ['quanben.net']
    start_urls = ['https://www.quanben.net/modules/article/articlelist.php?fullflag=1&page=1']

    pagelink = LinkExtractor(restrict_xpaths=('//a[@class="next"]'))

    rules = [
        Rule(pagelink, callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        item = QuanbenItem()
        li_list = response.xpath('//ul[@class="item-con"]/li')
        for li in li_list:
            item['name'] = li.xpath('./span[@class="s2"]/a/text()')[0].extract().strip()
            item['url'] = li.xpath('./span[@class="s2"]/a/@href')[0].extract().strip()
            item['category'] = li.xpath('./span[@class="s1"]/text()')[0].extract().strip()
            item['author'] = li.xpath('./span[@class="s3"]/text()')[0].extract().strip()
            item['update_date'] = li.xpath('./span[@class="s4"]/text()')[0].extract().strip()
            item['status'] = li.xpath('./span[@class="s5"]/text()')[0].extract().strip()

            yield item
















