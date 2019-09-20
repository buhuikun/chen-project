# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from photophotospider.items import PhotophotospiderItem



class PhotophotoSpider(CrawlSpider):
    name = 'photophoto'
    allowed_domains = ['photophoto.cn']

    start_urls = ['http://so.photophoto.cn/tag/%E6%B5%B7%E6%8A%A5']

    pageLink = LinkExtractor(restrict_xpaths=('//a[@class="pagenext"]'))
    contentLink = LinkExtractor(restrict_xpaths=('//div[@class="image"]/a'))

    rules = [
        Rule(pageLink, follow=True),
        Rule(contentLink, follow=True, callback='parse_item')
    ]

    def parse_item(self, response):
        title = response.xpath('//div[@id="left11"]/h1/text()')[0].extract().strip()
        print('title:', title)
        img = response.xpath('//div[@id="photo"]/img/@src')[0].extract().strip()

        item = PhotophotospiderItem()
        item['title'] = title
        item['image_url'] = img
        yield item
