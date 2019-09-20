# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from sunspider.items import SunspiderItem

class Sun3Spider(RedisCrawlSpider):
    name = 'sun3'

    redis_key = 'sun3:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(Sun3Spider, self).__init__(*args, **kwargs)

    # 定义规则
    # 翻页的链接提取器
    pagelink = LinkExtractor(restrict_xpaths=('//div[@class="pagination"]/a[text()=">"]'))

    # 帖子详情链接的提取器
    # contentlink = LinkExtractor(restrict_xpaths=('//a[@class="news14"]'))
    contentlink = LinkExtractor(restrict_css=('a.news14'))
    rules = [
        Rule(pagelink, follow=True),
        Rule(contentlink, callback='parse_item'),
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
