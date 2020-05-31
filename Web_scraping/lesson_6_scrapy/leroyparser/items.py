# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, Compose

def product_parameters(value):
    param_dict = {}
    for i in range(0, len(value), 2):
        param_dict[value[i]] = value[i + 1].split(sep='\n')[1][16:]
    return param_dict

def price_to_float(value):
    return float(value[0].replace(' ', ''))

def clear_name(value):
    return value[0].replace('/', '')

class LeroyparserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=Compose(clear_name))
    link = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(price_to_float), output_processor=TakeFirst())
    images = scrapy.Field()
    parameters = scrapy.Field(input_processor=Compose(product_parameters))
    pass
