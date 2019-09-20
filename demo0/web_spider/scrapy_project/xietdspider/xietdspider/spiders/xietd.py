# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from xietdspider.items import XietdspiderItem



class XietdSpider(CrawlSpider):
    name = 'xietd'
    allowed_domains = ['xietd.com']
    start_urls = ['http://www.xietd.com/forum-52-1.html']
    base_url = 'http://www.xietd.com/'
    pageLink = LinkExtractor(restrict_xpaths=('//a[@class="nxt"]'))
    contentLink = LinkExtractor(restrict_xpaths=('//div[@class="work-list-box"]//a[@class="card-img-hover"]'))

    rules = [
        Rule(pageLink, follow=True),
        Rule(contentLink, follow=True, callback='parse_item')
    ]


    def parse_item(self, response):

        title = response.xpath('//div[@class="details-contitle-box"]/h2/text()')[0].extract().strip()
        aimg = response.xpath('//div[@class="aimg"]')
        for a in range(len(aimg)):
            item = XietdspiderItem()
            img = aimg[a].xpath('./img/@zoomfile')[0].extract().strip()
            item['image_url'] = self.base_url+img
            item['title'] = title[:5]+str(a)
            yield item


