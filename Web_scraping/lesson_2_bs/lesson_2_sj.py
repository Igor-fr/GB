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

main_link = "https://www.superjob.ru"
vacancy = 'инженер'
params = {
    'keywords':vacancy
}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36',
          'Accept': '*/*'}

# Из массива по элементам собирваем строку и преобразуем в число
def parse_coast(mas):
    res = ''
    for m in mas:
        res += m
    return int(res)


df = pd.DataFrame(columns = ['Vacancy', 'Link', 'Company', 'City', 'Salary_min', 'Salary_max', 'Currency'])
i = 1
j = 0
while True:
    # Переход по страницам
    params['page'] = i
    i += 1
    response = requests.get(main_link + "/vacancy/search/", headers=header, params=params).text
    soup = bs(response, 'lxml')
    vac_list = soup.findAll('div', {'class': 'QiY08 LvoDO'})

    for vac in vac_list:

        vac_name = vac.find('div', {'class': '_3mfro CuJz5 PlM3e _2JVkc _3LJqf'}).getText()
        vac_link = main_link + vac.find('div', {'class':'_3mfro CuJz5 PlM3e _2JVkc _3LJqf'}).findChildren(recursive=False)[0]['href']
        vac_comp = np.nan
        if vac.find('span', {'class':'_3mfro _3Fsn4 f-test-text-vacancy-item-company-name _9fXTd _2JVkc _2VHxz _15msI'}):
            vac_comp = vac.find('span', {'class':'_3mfro _3Fsn4 f-test-text-vacancy-item-company-name _9fXTd _2JVkc _2VHxz _15msI'}).getText()
        vac_city = vac.find('span', {'class':'_3mfro f-test-text-company-item-location _9fXTd _2JVkc _2VHxz'}).getText().split(sep='•')[1]
        vac_salary = vac.find('span', {'class':'_3mfro _2Wp8I _31tpt f-test-text-company-item-salary PlM3e _2JVkc _2VHxz'}).getText()

        vac_salary_min = np.nan
        vac_salary_max = np.nan
        vac_salary_currency = np.nan
        
        # Разбиваем строку в зависимости от варианта указания зарплаты, если зарплата указана через дефис
        # то разделем строку по '-' на две стоимости, иначе откидываем присавку "от" или "до" и валюту,
        # и также передаем в функцию для получения стоимости
        if vac_salary.find('—') != -1:
            vac_salary_min = parse_coast(vac_salary.split(sep = '—')[0].split(sep = '\xa0'))
            vac_salary_max = parse_coast(vac_salary.split(sep = '—')[1].split(sep = '\xa0')[0:-1])
            vac_salary_currency = vac_salary.split(sep='\xa0')[-1]
        if vac_salary.find('от\xa0') != -1:
            vac_salary_min = parse_coast(vac_salary.split(sep = '\xa0')[1:-1])
            vac_salary_currency = vac_salary.split(sep='\xa0')[-1]
        if vac_salary.find('до\xa0') != -1:
            mm = vac_salary.split(sep = '\xa0')
            mm = mm[1:-1]
            vac_salary_max = parse_coast(vac_salary.split(sep = '\xa0')[1:-1])
            vac_salary_currency = vac_salary.split(sep='\xa0')[-1]

        df.loc[j] = [vac_name, vac_link, vac_comp, vac_city, vac_salary_min, vac_salary_max, vac_salary_currency]
        j += 1
        
    # Если кнопка дальше отсутствует - прекращаем парсинг
    if not soup.find('a', {'class': 'icMQ_ _1_Cht _3ze9n f-test-button-dalshe f-test-link-Dalshe'}):
        break

df.to_csv("sj.csv")
