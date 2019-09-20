from scrapy import cmdline

name = 'quanbenspider'

cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())