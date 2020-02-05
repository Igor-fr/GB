# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте "минимальный" и "максимальный отрицательный". Это два
# абсолютно разных значения.

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
    result = []
except ValueError:
    print("Верхнее число не должно быть меньше нижнего числа, до свидания.")
    exit()

max_negative = 0
idx = 0

for i, number in enumerate(first_list):
    if max_negative == 0 and number < 0:
        max_negative = number
        idx = i
    if max_negative != 0 and number < 0 and number > max_negative:
        max_negative = number
        idx = i


print(first_list)
if max_negative == 0:
    print("В сгенерированном массиве отсутстсовали отрицательные числа.")
else:
    print(f"Максимальное отрицательное число: {max_negative} на позиции: {idx}.")