# -*- coding: utf-8 -*-
import scrapy
from dytt.items import DyttItem

class DySpiderSpider(scrapy.Spider):
    name = 'dy_spider'
    allowed_domains = ['http://www.dytt8.net/html/gndy/dyzz/index.html']
    start_urls = ['http://www.dytt8.net']

    def parse(self, response):
        movie_list = response.xpath("//div[@class = 'co_content2']/ul/a")
        for i_item in movie_list:
            dy_item = DyttItem()
            dy_item['movie_name'] = i_item.xpath(".//div[@class = 'title_all']/h1").extract_first()
            print(movie_list)
            next_link = response.xpath("//div[@class = 'co_content2']/ul/a/@href").extract
            if next_link:
                yield scrapy.Request("http://www.dytt8.net"+next_link, callback=self.parse)
            # print(movie_list)

