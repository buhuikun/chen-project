from scrapy import cmdline

name = 'photophoto'

cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())
