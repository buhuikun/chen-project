import os
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline


class PhotophotospiderPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        print(item)
        image_url = item['image_url']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        print(results)
        if results[0][0]:
            image_path = results[0][1]['path']
            src = self.IMAGES_STORE + '/' + image_path
            dest = self.IMAGES_STORE + '/' + item['title'] + '.jpg'
            os.rename(src, dest)
            item['image_path'] = dest
            return item
