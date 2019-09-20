from scrapy import cmdline

name = 'douyuspider'

cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())