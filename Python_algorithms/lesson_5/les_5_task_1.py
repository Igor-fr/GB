# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

count = int(input("Введите количество предприятий: "))

Company = namedtuple('Company', 'name profit average_profit')
companies = []

for i in range(count):
    name = input(f"Введите название предприятия #{i+1}: ")
    profit = []
    for j in range(4):
        profit.append(int(input(f"Введите прибыль предприятия #{i+1} за {j+1} квартал: ")))
    companies.append(Company(name=name, profit=profit, average_profit=sum(profit)))

mid = sum([company.average_profit for company in companies])/count
print(f"Средняя прибыль всех предприятий за год: {mid}")

print(f"Предприятия с прибылью выше среднего:")
for c in companies:
    if c.average_profit > mid:
        print(f"{c.name}")

print(f"Предприятия с прибылью ниже среднего:")
for c in companies:
    if c.average_profit < mid:
        print(f"{c.name}")