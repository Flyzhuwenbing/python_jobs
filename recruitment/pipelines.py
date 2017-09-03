# -*- coding: utf-8 -*-
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
HOST = settings["HOST"]
PORT = settings["PORT"]
DB = settings["DB"]
COLLECTION1 = settings['COLLECTION1']
COLLECTION2 = settings["COLLECTION2"]

class python_lg(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            HOST,
            PORT
        )
        db = connection[DB]
        self.collection = db[COLLECTION1]
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
class python_zl(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            HOST,
            PORT
        )
        db = connection[DB]
        self.collection = db[COLLECTION2]
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()
    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item

