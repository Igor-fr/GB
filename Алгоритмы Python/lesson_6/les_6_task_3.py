# Вариант 3: с использованием словаря

import random
from sys import getsizeof

start = 1
end = 100
size = 200

first_list = [random.randint(start, end) for _ in range(size)]
result = {}

for item in first_list:
    if item in result.keys():
        result[item] += 1
    else:
        result[item] = 1
max = 0
max_frq = 0
for item in result.keys():
    if (result[item] > max_frq):
        max_frq = result[item]
        max = item

#Определение размера переменных
vars = list(globals().values())
total_size = 0
for var in vars:
    if isinstance(var, dict):
        total_size += getsizeof(var)
        for varkey, varvalue in var.items():
            total_size += getsizeof(varkey)
            total_size += getsizeof(varvalue)
    elif isinstance(var, list) or isinstance(var, tuple):
        total_size += getsizeof(var)
        for subvar in var:
            total_size += getsizeof(subvar)
    else:
        total_size += getsizeof(var)
print(f"Параметры генерируемого массива: начало: {start}, конец: {end}, размер: {size}. ")
print(f"Итоговый размер: {total_size} байт")

# Параметры генерируемого массива: начало: 1, конец: 10, размер: 20.
# Итоговый размер: 2621 байт

# Параметры генерируемого массива: начало: 1, конец: 10, размер: 200.
# Итоговый размер: 9125 байт

# Параметры генерируемого массива: начало: 1, конец: 100, размер: 200.
# Итоговый размер: 17997 байт

# С точки зрения использования памяти наиболее оптимальным оказывается второй вариант, где подсчет частоты вхождения
# происходит напрямую, используется минимум переменных и не хранятся лишние значения.
# На втором месте находится вариант с использованием массива, как наименее сложного объекта, и на третьем месте -
# словаря, при использовании которого требуемая память возрастает значительно быстрее, чем при использовании массива,
# как и ожидалось.