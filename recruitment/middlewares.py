# -*- coding: utf-8 -*-
import scrapy
import random
import requests
from scrapy import signals
# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

class ProxyMiddleWare(object):
    proxy_lst=[
        '183.232.65.203:3128',
        '24.200.102.149:8080',
        '162.243.18.46:3128',
        '119.9.105.210:9000',
        '183.232.65.202:3128',
    ]
    def process_request(self,request,spider):
        proxy = random.choice(self.proxy_lst).strip()
        request.meta['proxy'] = 'http://%s' % proxy

    '''def get_random_proxy(self):
        proxy_lst = []
        url = 'http://lab.crossincode.com/proxy/get/'
        req = requests.get(url)
        data = req.json()
        for p in data.get('proxies'):
            proxies = p.get('http')
            proxy_lst.append(proxies)
        proxy = random.choice(proxy_lst).strip()
        return proxy'''

class RecruitmentSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
