 # -*- coding: utf-8 -*-
import scrapy
from booksparser.items import BooksparserItem
from scrapy.http import HtmlResponse


class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']


    def __init__(self, name_books):
        self.start_urls = [f'https://www.labirint.ru/search/{name_books}']

    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[@title='Следующая']/@href").extract_first()

        book_links = response.xpath("//div[contains(@class,'card-column card-column_gutter')]//"
                                    "a[@class='product-title-link']/@href").extract()

        for link in book_links:
            yield response.follow(link, callback=self.book_parse)

        yield response.follow(next_page, callback=self.parse)



    def book_parse(self, response:HtmlResponse):
        authors = response.xpath("//div[@class='authors'][1]/a/text()").extract()
        name = response.xpath("//div[@class='prodtitle']/h1/text()").extract_first()
        link = response.url
        sale_coast = response.xpath("//span[@class='buying-pricenew-val-number']/text()").extract_first()
        old_coast = response.xpath("//span[@class='buying-priceold-val-number']/text()").extract_first()
        rating = response.xpath("//div[@id='rate']/text()").extract_first()
        yield BooksparserItem(authors=authors, name=name, link=link, sale_coast=sale_coast, old_coast=old_coast, rating=rating)