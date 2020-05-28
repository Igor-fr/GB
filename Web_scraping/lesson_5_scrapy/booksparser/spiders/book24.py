# -*- coding: utf-8 -*-
import scrapy
from booksparser.items import BooksparserItem
from scrapy.http import HtmlResponse


class Book24Spider(scrapy.Spider):
    name = 'book24'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/']

    def __init__(self, name_books):
        self.start_urls = [f'https://book24.ru/search/?q={name_books}']

    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[@class='catalog-pagination__item _text js-pagination-catalog-item']/@href").\
            extract()[-1]

        book_links = response.xpath("//div[@class='catalog-products__item js-catalog-products-item']"
                                    "//a[@class='book__image-link js-item-element ddl_product_link']/@href").extract()

        for link in book_links:
            yield response.follow(link, callback=self.book_parse)

        yield response.follow(next_page, callback=self.parse)




    def book_parse(self, response:HtmlResponse):
        authors = response.xpath("//a[@class='item-tab__chars-link js-data-link']/text()").extract()
        name = response.xpath("//h1[@class='item-detail__title']/text()").extract_first()
        link = response.url
        sale_coast = response.xpath("//div[@class='item-actions__price']/b/text()").extract_first()
        old_coast = response.xpath("//div[@class='item-actions__price-old']/text()").extract_first()
        rating = response.xpath("//span[@class='rating__rate-value']").extract_first()
        yield BooksparserItem(authors=authors, name=name, link=link, sale_coast=sale_coast, old_coast=old_coast, rating=rating)