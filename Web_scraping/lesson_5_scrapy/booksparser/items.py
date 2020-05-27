# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    authors = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    sale_coast = scrapy.Field()
    old_coast = scrapy.Field()
    rating = scrapy.Field()
    pass
