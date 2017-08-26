# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from recruitment.items import RecruitmentItem


class PythonZlSpider(scrapy.Spider):
    name = 'python_zl'
    start_urls = [
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E4%B8%8A%E6%B5%B7%2B%E5%B9%BF%E5%B7%9E%2B%E6%B7%B1%E5%9C%B3%2B%E5%A4%A9%E6%B4%A5&kw=python&p=1&isadv=0',
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%AD%A6%E6%B1%89%2B%E8%A5%BF%E5%AE%89%2B%E6%88%90%E9%83%BD%2B%E5%A4%A7%E8%BF%9E%2B%E9%95%BF%E6%98%A5&kw=python&p=1']
    for i in range(2, 3):
        start_urls.append(
            'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3%2B%E5%8C%97%E4%BA%AC%2B%E4%B8%8A%E6%B5%B7%2B%E5%B9%BF%E5%B7%9E%2B%E5%A4%A9%E6%B4%A5&kw=python&p={}'.format(
                i))
        start_urls.append(
            'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%AD%A6%E6%B1%89%2B%E8%A5%BF%E5%AE%89%2B%E6%88%90%E9%83%BD%2B%E5%A4%A7%E8%BF%9E%2B%E9%95%BF%E6%98%A5&kw=python&p={}'.format(
                i))

    def parse(self, response):
        links = response.xpath('//td[@class="zwmc"]//a/@href').extract()
        for link in links:
            yield Request(link, callback=self.get_Detail, dont_filter=True)

    def get_Detail(self, response):
        title = response.xpath('//div[@class="inner-left fl"]/h1/text()')[0].extract()
        salary = response.xpath('//ul[@class="terminal-ul clearfix"]//li[1]/strong/text()')[0].extract()
        area = response.xpath('//ul[@class="terminal-ul clearfix"]//li[2]/strong/a/text()')[0].extract()
        exp = response.xpath('//ul[@class="terminal-ul clearfix"]//li[5]/strong/text()')[0].extract()
        edu = response.xpath('//ul[@class="terminal-ul clearfix"]//li[6]/strong/text()')[0].extract()
        item = RecruitmentItem()
        item['title'] = title.strip()
        item['salary'] = salary.strip('\xa0')
        item['area'] = area
        item['exp'] = exp.strip()
        item['edu'] = edu.strip()
        yield item
