# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from sunspider.items import SunspiderItem


class Sun2Spider(RedisSpider):
    name = 'sun2'
    # allowed_domains = ['sun0769.com']
    # start_urls = ['http://sun0769.com/']
    redis_key = 'sun2:start_urls'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(Sun2Spider, self).__init__(*args, **kwargs)

    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0

    def parse(self, response):
        ls = response.xpath('//div[@class="greyframe"]/table[2]//table//tr')
        print('len:', len(ls))
        for each in ls:
            item = SunspiderItem()
            item['title'] = each.xpath('.//a[@class="news14"]/text()').extract()[0]
            item['number'] = each.xpath('./td[1]/text()').extract()[0]
            item['url'] = each.xpath('.//a[@class="news14"]/@href').extract()[0]
            item['author'] = each.xpath('./td[4]/text()').extract()[0]
            item['pub_date'] = each.xpath('./td[5]/text()').extract()[0]

            # 请求详情页面
            req = scrapy.Request(item['url'], callback=self.parse_item)
            req.meta['item'] = item
            yield req

        # 翻页
        if self.offset < 60000:
            self.offset += 30
            print('offset:', self.offset)
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parse_item(self, response):
        item = response.meta['item']
        # 投诉内容
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td/text()').extract()
        item['content'] = ''.join(item['content']).strip()
        yield item
