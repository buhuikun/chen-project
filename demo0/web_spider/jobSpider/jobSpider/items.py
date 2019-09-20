# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspiderItem(scrapy.Item):
    # 确定要爬取的目标
    # define the fields for your item here like:
    name = scrapy.Field()
    corp = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field()
    pub_date = scrapy.Field()


