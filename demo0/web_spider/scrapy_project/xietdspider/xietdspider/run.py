from scrapy import cmdline

name = 'xietd'

cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())
