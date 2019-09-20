import scrapy
from scrapy.pipelines.images import ImagesPipeline
import os
from scrapy.utils.project import get_project_settings


class XietdspiderPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        image_url = item['image_url']
        yield scrapy.Request(image_url)
        print('save...')

    def item_completed(self, results, item, info):
        print('aaaaa', results)
        if results[0][0]:
            image_path = results[0][1]['path']
            src = self.IMAGES_STORE + '/' + image_path
            dest = self.IMAGES_STORE + '/' + item['title'] + '.jpg'
            os.rename(src, dest)
            item['img_path'] = image_path
            yield item
