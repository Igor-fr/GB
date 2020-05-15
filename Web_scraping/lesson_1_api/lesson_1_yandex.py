# Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему,
# пройдя авторизацию. Ответ сервера записать в файл.

import requests
import json

main_link = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
key = 'trnsl.1.1.20200515T133519Z.3642b101d63a18c3.34d0610168e98b3849e923552d305d57537a024f'
text = "London is a capital of Great Britain"
lang = "en-ru"
params = {'key': key,
          'text': text,
          'lang': lang}

response = requests.get(main_link, params=params)

if response.ok:

    data = json.loads(response.text)
    print(f'Фраза \'{text}\' переводится как \'{data["text"][0]}\'')

# Переведено сервисом «Яндекс.Переводчик»