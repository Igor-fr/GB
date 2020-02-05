# Вариант 2: на основе прямого подсчета частоты встречаемости чисел и одновременного поиска максимальной частоты

import random
from sys import getsizeof

start = 1
end = 100
size = 200

first_list = [random.randint(start, end) for _ in range(size)]

max = 0
max_frq = 1
for i in range(size):
    frq_tmp = 1
    for k in range(i + 1, size):
        if first_list[i] == first_list[k]:
            frq_tmp += 1
    if frq_tmp > max_frq:
        max_frq = frq_tmp
        max = first_list[i]

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
# Итоговый размер: 1805 байт

# Параметры генерируемого массива: начало: 1, конец: 10, размер: 200.
# Итоговый размер: 8253 байт

# Параметры генерируемого массива: начало: 1, конец: 100, размер: 200.
# Итоговый размер: 8253 байт