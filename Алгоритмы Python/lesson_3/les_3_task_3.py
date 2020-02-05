# 3. В массиве случайных чисел поменять местами минимальный и максимальный элементы.

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

min = max = first_list[0]
idx_min = idx_max = 0

for i, number in enumerate(first_list):
    if number > max:
        max = number
        idx_max = i
    if number < min:
        min = number
        idx_min = i

print(first_list)

spam = first_list[idx_max]
first_list[idx_max] = first_list[idx_min]
first_list[idx_min] = spam

print(first_list)