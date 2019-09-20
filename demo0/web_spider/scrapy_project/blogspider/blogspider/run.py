from scrapy import cmdline

name = 'blogsina'

cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())
