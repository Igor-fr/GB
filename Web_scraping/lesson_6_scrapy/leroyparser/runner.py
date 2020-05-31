# 1) Взять любую категорию товаров на сайте Леруа Мерлен. Собрать с использованием ItemLoader следующие данные:
# ● название;
# ● все фото;
# ● параметры товара в объявлении.
# С использованием output_processor и input_processor реализовать очистку и преобразование данных. Цены должны быть
# в виде числового значения.
# 2)Написать универсальный обработчик параметров объявлений, который будет формировать данные вне зависимости от их
# типа и количества.
# 3)*Реализовать хранение скачиваемых файлов в отдельных папках, каждая из котоорых должна соответствовать собираемому
# товару

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from leroyparser import settings
from leroyparser.spiders.leroy import LeroySpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)

    product = 'доска'
    process.crawl(LeroySpider, product=product)
    process.start()