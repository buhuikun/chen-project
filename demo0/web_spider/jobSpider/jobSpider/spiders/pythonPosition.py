# -*- coding: utf-8 -*-
import re

import scrapy
from jobSpider.items import JobspiderItem


class PythonpositionSpider(scrapy.Spider):
    name = 'pythonPosition'  # 爬虫名称，唯一
    allowed_domains = ['51job.com']  # 允许爬取的域名
    start_urls = [
        'https://search.51job.com/list/010000,000000,0000,00,9,99,Python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def __init__(self):
        self.page = 1
        self.max_city = 40000
        self.city = 10000
        self.max_page = 3
        self.str1 = 'https://search.51job.com/list/0'
        self.str2 = ',000000,0000,00,9,99,Python,2,'
        self.str3 = '.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

    def get_url(self):
        return self.str1 + str(self.city) + self.str2 + str(self.page) + self.str3

    def parse(self, response):
        # 数据解析
        print('数据解析。。。。')
        job_ls = response.xpath('//div[@class="dw_table"]/div[@class="el"]')
        print('len:', len(job_ls))
        items = []
        for job in job_ls:
            name = job.xpath('./p/span/a/text()')[0].extract().strip()
            print('name:', name)
            corp = job.xpath('./span[@class="t2"]/a/text()')[0].extract().strip()
            print('corp:', corp)
            city = job.xpath('./span[@class="t3"]/text()')[0].extract().strip()
            print('city:', city)
            pub_date = job.xpath('./span[@class="t5"]/text()')[0].extract().strip()
            print('pub_date:', pub_date)
            salary = job.xpath('./span[@class="t4"]/text()').extract()
            if len(salary) > 0:
                salary = salary[0].strip()
            else:
                salary = '未知'

            print('salary:', salary)
            print('=' * 100)

            item = JobspiderItem()
            item['name'] = name
            item['city'] = city
            item['corp'] = corp
            item['salary'] = salary
            item['pub_date'] = pub_date

            yield item

        # 匹配当前url中的city，和page
        c = self.str1+r'(\d+).*'
        cur_city = re.search(c, response.url).group(1)
        p = self.str1+cur_city+self.str2+r'(\d+).*'
        cur_page = re.search(p, response.url).group(1)
        self.page = int(cur_page) + 1
        if self.page <= self.max_page:
            print('cur_page：', self.page)
            print('当前url', response.url)
            # 翻页
            url = self.get_url()
            # 发送新的url请求发送到请求等待队列
            yield scrapy.Request(url, callback=self.parse)
        else:
            self.city = int(cur_city) + 10000
            if self.city <= self.max_city:
                print('cur_city：', self.city)
                print('当前url', response.url)
                # 切换城市，切换到第一页
                self.page = 1
                url = self.get_url()
                yield scrapy.Request(url, callback=self.parse)
