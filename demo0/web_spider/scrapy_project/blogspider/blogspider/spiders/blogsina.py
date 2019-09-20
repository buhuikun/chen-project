# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from blogspider.items import BlogspiderItem


class BlogsinaSpider(CrawlSpider):
    name = 'blogsina'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1525875683_0_1.html']

    pagelink = LinkExtractor(restrict_xpaths=('//li[@class="SG_pgnext"]/a'))
    contentlink = LinkExtractor(restrict_xpaths=('//span[@class="atc_title"]/a'))

    rules = [
        Rule(pagelink, follow=True),
        Rule(contentlink, callback='parse_item')
    ]

    def parse_item(self, response):
        item = BlogspiderItem()
        item['title'] = response.xpath('//h2[@class="titName SG_txta"]/text()')[0].extract().strip()
        item['url'] = response.url

        yield item



















