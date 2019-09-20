from scrapy import cmdline

name = 'lianjia2'

cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())
