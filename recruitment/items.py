# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitmentItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    salary = scrapy.Field()
    area = scrapy.Field()
    exp = scrapy.Field()
    edu = scrapy.Field()

class python_lgItem(scrapy.Item):
    companyFullName = scrapy.Field()
    positonName = scrapy.Field()
    jobNature = scrapy.Field()
    workYear = scrapy.Field()
    district = scrapy.Field()
    firstType = scrapy.Field()
    formatCreateTime = scrapy.Field()
    companySize = scrapy.Field()
    education = scrapy.Field()
    industryField = scrapy.Field()
    positionLables = scrapy.Field()
    positionAdvantage = scrapy.Field()
    secondType = scrapy.Field()
    city = scrapy.Field()
    salary = scrapy.Field()
    companyLabelList = scrapy.Field()




