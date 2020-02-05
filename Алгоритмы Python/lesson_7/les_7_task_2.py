# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

array = [random.randint(0, 49) for _ in range(20)]


def merge_sort(array):

    n = len(array)

    if n <= 1:  # если разделили длину массива до отдельных элементов
        return array

    spam = n // 2  # делим массив на две части
    left = merge_sort(array[:spam])
    right = merge_sort(array[spam:])

    i = j = 0
    result = []
    len_left = len(left)
    len_right = len(right)

    while i < len_left or j < len_right:
        if i >= len_left:  # на случай если полностью прошли левую часть
            result.append(right[j])
            j += 1
        elif j >= len_right:  # на случай если полностью прошли правую часть
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:  # сравниваем первые элементы из обоих частей, добавляем меньший
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result

print(array)
print(merge_sort(array))