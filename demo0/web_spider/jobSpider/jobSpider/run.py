from scrapy import cmdline
# 作为程序入口

name = 'pythonPosition'
# 定义cmd命令
cmd = 'scrapy crawl {}'.format(name)
# 执行命令
cmdline.execute(cmd.split())




