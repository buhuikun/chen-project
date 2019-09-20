# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import codecs
# 数据存储

class JobspiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('51job.csv', 'w', encoding='utf-8')
        self.wr = csv.writer(self.file)
        self.wr.writerow(['name', 'city', 'corp', 'salary', 'pub_date'])

    def process_item(self, item, spider):

        self.wr.writerow([item['name'], item['city'], item['corp'], item['salary'], item['pub_date']])
        return item

    def close_spider(self, spider):
        self.file.close()

