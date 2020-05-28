# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class BooksparserPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_db = client.books

    def process_item(self, item, spider):
        if item['name'].find(':') != -1:
            item['name'] = item['name'].split(sep=':')[1]
        if item['authors']:
            item['authors'][-1] = item['authors'][-1].replace(' и др.', '')
        if item['sale_coast']:
            item['sale_coast'] = float(item['sale_coast'].replace(' ', ''))
        if item['old_coast']:
            item['old_coast'] = float(item['old_coast'].replace('р.', '').replace(' ', ''))
        if item['rating']:
            item['rating'] = float(item['rating'].replace(',','.'))
        collection = self.mongo_db[spider.name]
        collection.update_one({'link': item['link']}, {'$set': item},upsert=True)
        return item
