# 4. Определить, какое число в массиве встречается чаще всего.

import random

try:
    a = int(input("Введите нижнее число для генерируемого диапазона: "))
    b = int(input("Введите верхнее число для генерируемого диапазона: "))
    c = int(input("Введите количество генерируемых чисел: "))
except ValueError:
    print("В следующий раз вводите только целые числа, до свидания.")
    exit()

try:
    first_list = [random.randint(a, b) for _ in range(c)]
except ValueError:
    print("Верхнее число не должно быть меньше нижнего числа, до свидания.")
    exit()

min = max = 0 # действия с 19 по 27 строчку нужны на случай, если бы мы не знали, какой диапазон чисел в массиве

for number in first_list:
    if number > max:
        max = number
    if number < min:
        min = number

result = [0 for _ in range(min, max + 1)]

for number in first_list:
    result[number - min] += 1 #сдвигаем индексы, чтобы наше минимальное число соответствовало нулевому индексу

max_res = result[0]
idx_max = 0

for i, number in enumerate(result): # поиск - какое число встретилось чаще всего (значение - частота - индекс (+а) - само число)
    if number > max_res:
        max_res = number
        idx_max = i

print(first_list)
print(result)
print(f"Число {idx_max + min} встретилось {max_res} раз.") #сдвигаем индексы обратно