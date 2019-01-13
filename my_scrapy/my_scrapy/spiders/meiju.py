# -*- coding: utf-8 -*-
import scrapy
from my_scrapy.items import MyScrapyItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = MyScrapyItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            yield item
