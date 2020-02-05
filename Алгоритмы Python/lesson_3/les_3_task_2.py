# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля)
# т.к. именно в этих позициях первого массива стоят четные числа.

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

result = []

for i, number in enumerate(first_list):
    if number % 2 == 0:
        result.append(i)

print(first_list)
print(result)