# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunspider.items import SunspiderItem


class Sun1Spider(CrawlSpider):
    name = 'sun1'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    pagelink = LinkExtractor(restrict_xpaths=('//span[@class="pagination"]/a[last()-1]'))
    contentlink = LinkExtractor(restrict_xpaths=('//a[@class="news14"]'))

    rules = [
        Rule(pagelink, follow=True),
        Rule(contentlink, follow=True, callback='parse_item')
    ]


    def parse_item(self, response):
        # 从详情页面中提取数据
        item = SunspiderItem()
        # 标题
        item['title'] = \
            response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[1]/text()').extract()[0].strip().split('：')[-1]
        # 编号
        item['number'] = \
            response.xpath('//div[@class="wzy1"]/table[1]//td[2]/span[2]/text()').extract()[0].strip().split(':')[-1]
        # url
        item['url'] = response.url
        # 投诉内容
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td/text()').extract()
        item['content'] = ''.join(item['content']).strip()
        # 投诉者
        temp = response.xpath('//div[@class="wzy3_2"]/span/text()').extract()[0].strip()
        temp = temp.split(' ')
        item['author'] = temp[0].split('：')[-1]
        item['pub_date'] = temp[1].split('：')[-1]

        yield item








