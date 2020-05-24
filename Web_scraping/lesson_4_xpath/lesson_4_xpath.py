# 1)Написать приложение, которое собирает основные новости с сайтов news.mail.ru, lenta.ru, yandex.news
# Для парсинга использовать xpath. Структура данных должна содержать:
# * название источника,
# * наименование новости,
# * ссылку на новость,
# * дата публикации
# 2)Сложить все новости в БД

from lxml import html
import requests
from datetime import datetime
from datetime import timedelta
from pymongo import MongoClient
from pprint import pprint
import pandas as pd

header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                        "81.0.4044.138 Safari/537.36"}

# Парсер datetime не воспринимает родительный падеж русских названий месяца
months = {
    'января':'1',
    'ферваля':'2',
    'марта': '3',
    'апреля': '4',
    'мая': '5',
    'июня': '6',
    'июля': '7',
    'августа': '8',
    'сентября': '9',
    'октября': '10',
    'ноября': '11',
    'декабря': '12'
}

def yandex_news():

    main_link = "https://yandex.ru/news"

    response = requests.get(main_link, headers=header)
    dom = html.fromstring(response.text)

    dates = dom.xpath("//div[@class='story__date']/text()")
    titles = dom.xpath("//h2[@class='story__title']/a/text()")
    links = dom.xpath("//h2[@class='story__title']/a/@href")

    results = []
    for i in range(len(dates)):
        # В строке с датой и источником вся информация разделена пробелами если там указаны только источник и сегодняшнее
        # время, но если там указана прошедшая дата или написано "вчера", то в строке появляются символы "\xa0",
        # на основании которых и будем получать корректную дату
        news_time = dates[i].split(sep=' ')[-1]
        if news_time.find('\xa0') != -1:
            # Если есть слово "вчера" - записываем вчерашнюю дату
            if news_time.find('вчера') != -1:
                news_date = datetime.now() - timedelta(days=1)
                news_time = news_time.split(sep='\xa0')[-1]
                news_date = datetime.strptime(str(news_date.day) + '.' + str(news_date.month) + '.' + str(news_date.year)
                                              + ' ' + news_time, "%d.%m.%Y %H:%M")
            # Если есть символы "\xa0", но нет слова вчера, значит указана конкретная дата, заменяем месяц в соответствии
            # со словарем, день получаем из строки
            else:
                str_date = news_time.split(sep='\xa0')[0] + '.' + months[news_time.split(sep='\xa0')[1]] + '.' + \
                           str(datetime.now().year) + ' ' + news_time.split(sep='\xa0')[-1]
                news_date = datetime.strptime(str_date, "%d.%m.%Y %H:%M")
        # Если никаких символов нет и просто указан источник и время сегодняшнего дня
        else:
            news_date = datetime.now()
            day = str(news_date.day)
            month = str(news_date.month)
            year = str(news_date.year)
            str_date = day + '.' + month + '.' + year + ' ' + news_time
            news_date = datetime.strptime(str_date, "%d.%m.%Y %H:%M")

        news = {
            'date': news_date,
            'source': dates[i].replace(dates[i].split(sep=' ')[-1], ''),
            'title': titles[i].replace('\n', ' ').replace('\xa0', ' '),
            'link': "https://yandex.ru" + links[i]
        }
        results.append(news)
    return results


def lenta_news():

    main_link = "https://lenta.ru"

    response = requests.get(main_link, headers=header)
    dom = html.fromstring(response.text)

    # Два пути, чтобы также звахватить главную новость, которая идет первой и с изображением
    dates = dom.xpath("//div[contains(@class,'main__content')]//div[@class='item']/a/time/@datetime "
                      "| //div[@class='first-item']//time/@datetime")
    titles = dom.xpath("//div[contains(@class,'main__content')]//div[@class='item']/a/text() "
                      "| //div[@class='first-item']/h2/a/text()")
    links = dom.xpath("//div[contains(@class,'main__content')]//div[@class='item']/a/@href "
                     "| //div[@class='first-item']/h2/a/@href")

    results = []

    for i in range(len(dates)):
        date = dates[i].split(sep=' ')
        month = months[date[3]]
        dates[i] = dates[i].replace(date[3], month)
        news_date = datetime.strptime(dates[i], " %H:%M, %d %m %Y")
        news = {
            'date': news_date,
            'source': 'Lenta.ru',
            'link': main_link + links[i],
            'title': titles[i].replace('\n', ' ').replace('\xa0', ' ')
        }
        results.append(news)
    return results


def mail_news():

    main_link = "https://news.mail.ru"

    response = requests.get(main_link, headers=header)
    dom = html.fromstring(response.text)

    # Два пути, чтобы также звахватить первые несколько новостей, идущих первыми с изображением
    links = dom.xpath("//div[contains(@class,'daynews__item')]//a/@href | //li[contains(@class,'item')]//a/@href")

    results = []

    for link in links:

        if link.find("https") == -1:
            link = main_link + link
        response = requests.get(link, headers=header)
        dom = html.fromstring(response.text)

        date = dom.xpath("//span[@class='note__text breadcrumbs__text js-ago']/@datetime")
        title = dom.xpath("//h1[@class='hdr__inner']/text()")[0].replace('\n', ' ').replace('\xa0', ' ')
        source = dom.xpath("//a[@class='link color_gray breadcrumbs__link']/span/text()")
        title = title

        str_date = date[0].replace('T', ' ').split(sep='+')
        news_date = datetime.strptime(str_date[0], "%Y-%m-%d %H:%M:%S")

        news = {
            'date': news_date,
            'source': source[0],
            'link': link,
            'title': title
        }
        results.append(news)
    return results

data = yandex_news() + lenta_news() + mail_news()

client = MongoClient('localhost', 27017)
news_db = client['news']
news_collection = news_db.news

# Проверяем по ссылке, если такой ссылки еще не было - записываем, если была - перезаписываем
for row in data:
    news_collection.update_one({'link':row['link']},{'$set':row}, upsert=True)

# Выведем все заголовки и сохраним данные в .csv
all_news = news_collection.find({})
df = pd.DataFrame(columns = ['Title', 'Date', 'Link', 'Source'])
for i, news in enumerate(all_news):
    pprint(news['title'])
    df.loc[i] = [news['title'], news['date'], news['link'], news['source']]
df.to_csv("news.csv")

# Выведем количество документов
print(news_collection.estimated_document_count())