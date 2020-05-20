from pymongo import MongoClient
import pandas as pd
from hashlib import sha1
from pprint import pprint

# Подключаемся к БД
client = MongoClient('localhost', 27017)
db = client['vacancy_db']
hh = db.hh
sj = db.sj


# Загружаем датафреймы
hh_df = pd.read_csv("hh.csv")
sj_df = pd.read_csv("sj.csv")


# Функция поиска зарплаты - либо минимальная, либо максимальная, либо обе зарплаты должны быть больше введенной суммы
def print_salary_limit(collection, limit):
    vacancies = collection.find({'$or': [{'salary_min':{'$gt':limit}}, {'salary_max':{'$gt':limit}}]})
    for vacancy in vacancies:
        pprint(vacancy)


# Принимаем датафрейм и коллекцию, получаем список id из коллекции. Для каждой порции данных по всем имеющимся в ней
# данным вычисляем sha, проверяем нет ли такого sha в полученных id из коллекции, если нет - добавляем порцию в БД,
# иначе переходим к следующей порции
def add_dataframe_to_mongo(df, collection):

    collections_id = [id['_id'] for id in collection.find({}, {'_id': 1})]

    for i in range(df.shape[0]):
        row_vac = df.loc[i]
        sha = sha1(str(row_vac).encode('utf-8')).hexdigest()

        if sha in collections_id:
            continue

        dic = {
            '_id':              sha,
            'vacancy':          row_vac['Vacancy'],
            'link':             row_vac["Link"],
            'company':          row_vac["Company"],
            'city':             row_vac["City"],
            'salary_min':       row_vac["Salary_min"],
            'salary_max':       row_vac['Salary_max'],
            'salary_currency':  row_vac["Currency"]
        }
        collection.insert_one(dic)

# Сначала добавили по 50 строк из датафреймов от 0 до 50, убедились что количество записей в БД стало по 51
# add_to_mongo(hh_df.loc[0:50], hh)
# add_to_mongo(sj_df.loc[0:50], sj)

# Затем добавили по 150 строк из датафреймов от 0 до 150, убедились что количество записей в БД стало по 151.
# Соответственно записи не дублируются.
# add_to_mongo(hh_df.loc[0:150], hh)
# add_to_mongo(sj_df.loc[0:150], sj)

# Загружаем оставшиеся данные в полном объеме, проверям количество записей в БД - все верно, количество записей в БД
# совпадает с количеством записей в выгруженных датафреймах (hh - 2000, sj - 374), дубликатов нет.
add_dataframe_to_mongo(hh_df, hh)
add_dataframe_to_mongo(sj_df, sj)
print(hh.estimated_document_count(), sj.estimated_document_count())


# Выводим вакансии с зарплатой более чем 150 тыс. и 100 тыс. соответственно.
print_salary_limit(hh, 150000)
print('______________')
print_salary_limit(sj, 100000)