from scrapy import cmdline
# name = 'sun1'
# name = 'sun2'
name = 'sun3'


cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())

