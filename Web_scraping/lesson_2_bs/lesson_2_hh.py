# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы) с сайта
# superjob.ru и hh.ru. Приложение должно анализировать несколько страниц сайта(также вводим через input или аргументы).
# Получившийся список должен содержать в себе минимум:
# *Наименование вакансии
# *Предлагаемую зарплату (отдельно мин. отдельно макс. и отдельно валюту)
# *Ссылку на саму вакансию
# *Сайт откуда собрана вакансия
# По своему желанию можно добавить еще работодателя и расположение. Данная структура должна быть одинаковая для
# вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas.

from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import pandas as pd

main_link = "https://hh.ru/search/vacancy"
vacancy = 'python'
params = {
    'area':'1',
    'st': 'searchVacancy',
    'text': vacancy
}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36',
          'Accept': '*/*'}


def parse_coast(str):
    mas = str.split(sep=u'\xa0')
    res = ''
    for m in mas:
        res += m
    return int(res)


df = pd.DataFrame(columns = ['Vacancy', 'Link', 'Company', 'City', 'Salary_min', 'Salary_max', 'Currency'])
i = 0
j = 0
while True:

    params['page'] = i
    i += 1
    response = requests.get(main_link, headers=header, params=params).text
    soup = bs(response, 'lxml')
    vac_list = soup.findAll('div', {'class': 'vacancy-serp-item'})

    for vac in vac_list:

        vac_name = vac.find('a', {'class':'bloko-link HH-LinkModifier'}).getText()
        vac_link = vac.find('a', {'class':'bloko-link HH-LinkModifier'})['href']
        vac_comp = vac.find('div', {'class':'vacancy-serp-item__meta-info'}).getText()
        vac_city = vac.find('span', {'class':'vacancy-serp-item__meta-info'}).getText()
        vac_salary = vac.find('div', {'class':'vacancy-serp-item__sidebar'}).getText()

        vac_salary_min = np.nan
        vac_salary_max = np.nan
        vac_salary_currency = np.nan

        if vac_salary.find('-') != -1:
            vac_salary_min = parse_coast(vac_salary.split(sep = ' ')[0].split(sep='-')[0])
            vac_salary_max = parse_coast(vac_salary.split(sep = ' ')[0].split(sep='-')[1])
            vac_salary_currency = vac_salary.split(sep=' ')[-1]
        if vac_salary.find('от') != -1:
            vac_salary_min = parse_coast(vac_salary.split(sep = ' ')[1])
            vac_salary_currency = vac_salary.split(sep=' ')[-1]
        if vac_salary.find('до') != -1:
            vac_salary_max = parse_coast(vac_salary.split(sep = ' ')[1])
            vac_salary_currency = vac_salary.split(sep=' ')[-1]

        df.loc[j] = [vac_name, vac_link, vac_comp, vac_city, vac_salary_min, vac_salary_max, vac_salary_currency]
        j += 1

    if not soup.find('a', {'class': 'HH-Pager-Controls-Next'}):
        break

df.to_csv("hh.csv")