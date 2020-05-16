# РќРµРѕР±С…РѕРґРёРјРѕ СЃРѕР±СЂР°С‚СЊ РёРЅС„РѕСЂРјР°С†РёСЋ Рѕ РІР°РєР°РЅСЃРёСЏС… РЅР° РІРІРѕРґРёРјСѓСЋ РґРѕР»Р¶РЅРѕСЃС‚СЊ (РёСЃРїРѕР»СЊР·СѓРµРј input РёР»Рё С‡РµСЂРµР· Р°СЂРіСѓРјРµРЅС‚С‹) СЃ СЃР°Р№С‚Р°
# superjob.ru Рё hh.ru. РџСЂРёР»РѕР¶РµРЅРёРµ РґРѕР»Р¶РЅРѕ Р°РЅР°Р»РёР·РёСЂРѕРІР°С‚СЊ РЅРµСЃРєРѕР»СЊРєРѕ СЃС‚СЂР°РЅРёС† СЃР°Р№С‚Р°(С‚Р°РєР¶Рµ РІРІРѕРґРёРј С‡РµСЂРµР· input РёР»Рё Р°СЂРіСѓРјРµРЅС‚С‹).
# РџРѕР»СѓС‡РёРІС€РёР№СЃСЏ СЃРїРёСЃРѕРє РґРѕР»Р¶РµРЅ СЃРѕРґРµСЂР¶Р°С‚СЊ РІ СЃРµР±Рµ РјРёРЅРёРјСѓРј:
# *РќР°РёРјРµРЅРѕРІР°РЅРёРµ РІР°РєР°РЅСЃРёРё
# *РџСЂРµРґР»Р°РіР°РµРјСѓСЋ Р·Р°СЂРїР»Р°С‚Сѓ (РѕС‚РґРµР»СЊРЅРѕ РјРёРЅ. РѕС‚РґРµР»СЊРЅРѕ РјР°РєСЃ. Рё РѕС‚РґРµР»СЊРЅРѕ РІР°Р»СЋС‚Сѓ)
# *РЎСЃС‹Р»РєСѓ РЅР° СЃР°РјСѓ РІР°РєР°РЅСЃРёСЋ
# *РЎР°Р№С‚ РѕС‚РєСѓРґР° СЃРѕР±СЂР°РЅР° РІР°РєР°РЅСЃРёСЏ
# РџРѕ СЃРІРѕРµРјСѓ Р¶РµР»Р°РЅРёСЋ РјРѕР¶РЅРѕ РґРѕР±Р°РІРёС‚СЊ РµС‰Рµ СЂР°Р±РѕС‚РѕРґР°С‚РµР»СЏ Рё СЂР°СЃРїРѕР»РѕР¶РµРЅРёРµ. Р”Р°РЅРЅР°СЏ СЃС‚СЂСѓРєС‚СѓСЂР° РґРѕР»Р¶РЅР° Р±С‹С‚СЊ РѕРґРёРЅР°РєРѕРІР°СЏ РґР»СЏ
# РІР°РєР°РЅСЃРёР№ СЃ РѕР±РѕРёС… СЃР°Р№С‚РѕРІ. РћР±С‰РёР№ СЂРµР·СѓР»СЊС‚Р°С‚ РјРѕР¶РЅРѕ РІС‹РІРµСЃС‚Рё СЃ РїРѕРјРѕС‰СЊСЋ dataFrame С‡РµСЂРµР· pandas.

from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import pandas as pd

main_link = "https://www.superjob.ru"
vacancy = 'РёРЅР¶РµРЅРµСЂ'
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
        vac_city = vac.find('span', {'class':'_3mfro f-test-text-company-item-location _9fXTd _2JVkc _2VHxz'}).getText().split(sep='вЂў')[1]
        vac_salary = vac.find('span', {'class':'_3mfro _2Wp8I _31tpt f-test-text-company-item-salary PlM3e _2JVkc _2VHxz'}).getText()

        vac_salary_min = np.nan
        vac_salary_max = np.nan
        vac_salary_currency = np.nan

        # Разбиваем строку в зависимости от варианта указания зарплаты, если зарплата указана через дефис
        # то разделем строку по '-' на две стоимости, иначе откидываем присавку "от" или "до" и валюту,
        # и также передаем в функцию для получения стоимости
        if vac_salary.find('вЂ”') != -1:
            vac_salary_min = parse_coast(vac_salary.split(sep = 'вЂ”')[0].split(sep = '\xa0'))
            vac_salary_max = parse_coast(vac_salary.split(sep = 'вЂ”')[1].split(sep = '\xa0')[0:-1])
            vac_salary_currency = vac_salary.split(sep='\xa0')[-1]
        if vac_salary.find('РѕС‚\xa0') != -1:
            vac_salary_min = parse_coast(vac_salary.split(sep = '\xa0')[1:-1])
            vac_salary_currency = vac_salary.split(sep='\xa0')[-1]
        if vac_salary.find('РґРѕ\xa0') != -1:
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