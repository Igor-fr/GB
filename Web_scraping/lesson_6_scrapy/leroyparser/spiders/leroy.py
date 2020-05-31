# -*- coding: utf-8 -*-
import scrapy
from leroyparser.items import LeroyparserItem
from scrapy.loader import ItemLoader


class LeroySpider(scrapy.Spider):
    name = 'leroy'
    allowed_domains = ['leroymerlin.ru']
    start_urls = ['http://leroymerlin.ru/']

    def __init__(self, product):
        self.start_urls = [f'https://leroymerlin.ru/search/?q={product}']

    def parse(self, response):
        next_page = response.xpath("//div[@class='next-paginator-button-wrapper']/a[1]/@href").extract_first()
        product_links = response.xpath("//div[@class='product-name']/a/@href").extract()

        for link in product_links:
            yield response.follow(link, callback=self.product_parse)

        yield response.follow(next_page, callback=self.parse)

    def product_parse(self, response):
        loader = ItemLoader(item=LeroyparserItem(), response=response)
        loader.add_xpath('name', "//h1[@slot='title']/text()")
        loader.add_value('link', response.url)
        loader.add_xpath('price', "//uc-pdp-price-view[@slot='primary-price']/span[@slot='price']/text()")
        loader.add_xpath('images', "//picture[@slot='pictures']/source[1]/@srcset")
        loader.add_xpath('parameters', "//dt[@class='def-list__term']/text() | //dd[@class='def-list__definition']"
                                       "/text()")
        yield loader.load_item()
