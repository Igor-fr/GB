# Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import json

user = 'igor-fr'
main_link = 'https://api.github.com/users/'

response = requests.get(f'{main_link}{user}/repos')
repos = response.json()

if response.ok:

    for i, repo in enumerate(repos):
        print(f'{i+1}.\t {repo["name"]}')

    with open(f'{user}_repos.json', 'w', encoding='utf-8') as f:
        json.dump(repos, f, indent=4, ensure_ascii=False)