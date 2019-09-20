from scrapy import cmdline

name = 'Qiushi'

cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())