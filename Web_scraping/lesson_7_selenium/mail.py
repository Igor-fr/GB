from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from datetime import timedelta
from pymongo import MongoClient

months = {
    'января':'1',
    'февраля':'2',
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

client = MongoClient('localhost', 27017)
letters_db = client['letters']
letters_collection = letters_db.letters

driver = webdriver.Chrome('/Users/igorfrolkin/PycharmProjects/lesson_7_selenium/chromedriver')
driver.maximize_window()
driver.get('https://account.mail.ru/login')

# time.sleep(1)


WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'login-header'))
)
elem = driver.find_element_by_name('username')
elem.send_keys('study.ai_172@mail.ru')
elem.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'login-header'))
)

elem = driver.find_element_by_name('password')
elem.send_keys('NextPassword172')
elem.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'portal-menu__logo__img'))
)
count_letters = driver.find_element_by_xpath("//a[contains(@class, 'nav__item js-shortcut nav__item_active')]").\
    get_attribute("title")
count_letters = int(count_letters.split(sep = ' ')[1])
letters = driver.find_elements_by_xpath("//a[contains(@class, 'llc')]")
written_letters = []
i = 0
j = 0
results = []
while i < count_letters:
    actions = ActionChains(driver)
    if letters[j] not in written_letters:
        written_letters.append(letters[j])
        actions.key_down(Keys.COMMAND).click(letters[j]).key_up(Keys.COMMAND).perform()

        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'letter__author'))
        )
        texts = driver.find_elements_by_xpath("//div[@class='letter__body']//tbody//span | "
                                               "//div[@class='letter__body']//p")
        letter_text = []
        for text in texts:
            letter_text.append(text.text)
        author_mail = driver.find_element_by_xpath("//div[@class='letter__author']//span[@class='letter-contact']").\
            get_attribute("title")
        author_name = driver.find_element_by_xpath("//div[@class='letter__author']//span[@class='letter-contact']").text
        theme = driver.find_element_by_xpath("//h2[@class='thread__subject thread__subject_pony-mode']").text
        date = driver.find_element_by_xpath("//div[@class='letter__date']").text
        if date.find('Сегодня') != -1:
            letter_date = datetime.now()
            hour = date.split(sep = ' ')[1].split(sep=':')[0]
            minute = date.split(sep=' ')[1].split(sep=':')[1]
            day = str(letter_date.day)
            month = str(letter_date.month)
            year = str(letter_date.year)
            str_date = day + '.' + month + '.' + year + ' ' + hour + ':' + minute
            letter_date = datetime.strptime(str_date, "%d.%m.%Y %H:%M")
        elif date.find('Вчера') != -1:
            letter_date = datetime.now() - timedelta(days=1)
            hour = date.split(sep=' ')[1].split(sep=':')[0]
            minute = date.split(sep=' ')[1].split(sep=':')[1]
            day = str(letter_date.day)
            month = str(letter_date.month)
            year = str(letter_date.year)
            str_date = day + '.' + month + '.' + year + ' ' + hour + ':' + minute
            letter_date = datetime.strptime(str_date, "%d.%m.%Y %H:%M")
        else:
            letter_date = datetime.now()
            hour = date.split(sep=' ')[-1].split(sep=':')[0]
            minute = date.split(sep=' ')[-1].split(sep=':')[1]
            day = date.split(sep=' ')[0]
            month = months[date.split(sep=' ')[1].replace(',', '')]
            year = str(letter_date.year)

            if len(date.split(sep = ' ')) == 4:
                year = date.split(sep=' ')[2].replace(',', '')

            str_date = day + '.' + month + '.' + year + ' ' + hour + ':' + minute
            letter_date = datetime.strptime(str_date, "%d.%m.%Y %H:%M")
        letter = {
            'date': letter_date,
            'author_mail': author_mail,
            'author_name': author_name,
            'theme': theme,
            'text': letter_text
        }
        letters_collection.update_one({'date': letter['date']}, {'$set': letter}, upsert=True)
        results.append(letter)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        i += 1
        j += 1
    else:
        j += 1
    if j == len(letters):

        letters = driver.find_elements_by_xpath("//a[contains(@class, 'llc')]")
        j = 0

print(len(written_letters))