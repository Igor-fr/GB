from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
mvideo_db = client['mvideo']
mvideo_collection = mvideo_db.mvideo

driver = webdriver.Chrome('/Users/igorfrolkin/PycharmProjects/lesson_7_selenium/chromedriver')
driver.maximize_window()
driver.get('https://www.mvideo.ru/')

time.sleep(5)

while True:
    try:
        button = driver.find_element_by_xpath("//div[@class='gallery-layout'][2]//a[@class='next-btn sel-hits-button-next']")
        button.click()
    except:
        break

sales = driver.find_elements_by_xpath("//div[@class='gallery-layout'][2]//li[@class='gallery-list-item height-ready']//a[@class='sel-product-tile-title']")
actions = ActionChains(driver)
for sale in sales:
    item = sale.get_attribute("data-product-info")
    item = item.replace('\n', '')
    item = item.replace('\t', '')
    item = json.loads(item)
    item = {
        'name': item['productName'],
        'price': float(item['productPriceLocal'])
    }
    mvideo_collection.update_one({'name': item['name']}, {'$set': item}, upsert=True)