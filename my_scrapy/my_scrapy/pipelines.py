# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
print (os.path.abspath('..'))
class MyScrapyPipeline(object):
    def process_item(self, item, spider):
        with open(os.path.abspath('..')+'\my_meiju.txt','a') as fp:
            fp.write(item['name'].encode('utf-8')+'\n')
