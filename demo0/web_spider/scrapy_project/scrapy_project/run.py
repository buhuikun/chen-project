from scrapy import cmdline
name = 'bilibili'
# name = 'people'
# name = 'sun'
# name = 'yangtse'

cmd = 'scrapy crawl {}'.format(name)

cmdline.execute(cmd.split())

