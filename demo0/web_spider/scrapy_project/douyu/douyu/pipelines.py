
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from scrapy.utils.project import get_project_settings


class DouyuPipeline(ImagesPipeline):
    # 使用settings中定义的路径常量，
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_url = item['image_url']

        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 当照片下载结束时会触发这个方法
        if results[0][0]:
            image_path = results[0][1]['path']
            src = self.IMAGES_STORE + '/' + image_path
            dest = self.IMAGES_STORE + '/' + item['name'] + '.jpg'
            # 图片重命名
            os.rename(src, dest)
            item['image_path'] = dest
            return item
