# -*- coding: utf-8 -*-
import scrapy


class PythonLgSpider(scrapy.Spider):
    name = 'python_lg'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']

    def parse(self, response):
        pass
