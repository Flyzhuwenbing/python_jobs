# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import log
from recruitment.items import python_lgItem

class PythonLgSpider(scrapy.Spider):
    name = 'python_lg'
    custom_settings = {
        'ITEM_PIPELINES': {
        'recruitment.pipelines.python_lg': 200,
    }
    }
    allowed_domains = ['lagou.com']
    headers = {
        'Content - Type': 'application / json;charset = UTF - 8',
        'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh;q = 0.8',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
    }

    def start_requests(self):
        for i in range(1,3):
            yield scrapy.FormRequest(
                'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false',
                formdata={'pn': str(i), 'kd': 'python'}, method='POST', headers=self.headers)

    def parse(self, response):
        try:
            data =response.body.decode('utf-8')# 将bytes对象转为str
            html = json.loads(data)
        except ValueError:
            log.msg(response.body, level = log.ERROR)
            log.msg(response.status,level = log.ERROR)
            yield scrapy.FormRequest(response.url,headers=self.headers,formdata={'pn':str(response.meta.get('page')),'kd':'python'},meta={'page':response.meta.get('page'),'kd':'python'},dont_filter=True) # ,formdata={'pn':str(response.meta.get('page')),'kd':'python'},headers=self.headers,meta={'page':response.meta.get('page'),'kd':'python'
        results = html.get('content').get('positionResult').get('result')
        for result in results:
            item = python_lgItem()
            item['companyFullName'] = result.get('companyFullName')
            item['positonName'] = result.get('companyFullName')
            item['jobNature'] = result.get('jobNature')
            item['workYear'] = result.get('workYear')
            item['district'] = result.get('district')
            item['firstType'] = result.get('firstType')
            item['formatCreateTime'] = result.get('formatCreateTime')
            item['companySize'] = result.get('companySize')
            item['edution'] = result.get('edution')
            item['industryField'] = result.get('industryField')
            item['positionLables'] = result.get('positionLables')
            item['positionAdvantage'] = result.get('positionAdvantage')
            item['secondType'] = result.get('secondType')
            item['city'] = result.get('city')
            item['salary'] = result.get('salary')
            item['companyLabelList'] = result.get('companyLabelList')
            yield item







