# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Выбрано задание 4 из 3 урока, а именно:
# Определить, какое число в массиве встречается чаще всего.

# Вариант 1: на основе использования массива, где каждая ячейка будет хранить частоту соответствующего числа

import random
from sys import getsizeof

start = 1
end = 100
size = 200

first_list = [random.randint(start, end) for _ in range(size)]
result = [0 for _ in range(start, end + 1)]

for number in first_list:
    result[number - start] += 1

max = 0
max_frq = 0

for i in range(len(result)):
    if result[i] > max_frq:
        max_frq = result[i]
        max = i + start

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

# Информация о версии и платформе:
# 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21)
# [Clang 6.0 (clang-600.0.57)] darwin


# Параметры генерируемого массива: начало: 1, конец: 10, размер: 20.
# Итоговый размер: 2329 байт

# Параметры генерируемого массива: начало: 1, конец: 10, размер: 200.
# Итоговый размер: 8777 байт

# Параметры генерируемого массива: начало: 1, конец: 100, размер: 200.
# Итоговый размер: 11885 байт