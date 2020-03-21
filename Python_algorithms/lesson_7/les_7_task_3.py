# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
# не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).


import random

m = 0
array = [random.randint(0, 49) for _ in range(2 * m + 1)]

def mediana(array, k):

    if len(array) == 1 and k == 0:
        return array[0]

    element = random.choice(array)

    less = []
    more = []
    equals = []
    for i in array:
        if i < element:
            less.append(i)
        elif i > element:
            more.append(i)
        else:
            equals.append(i)

    if k < len(less):
        return mediana(less, k)
    elif k < len(less) + len(equals):
        return element
    else:
        return mediana(more, k - len(less) - len(equals))


print(array)
print(mediana(array, len(array) // 2))
print(sorted(array))  # для наглядности

# Логика в том, что выбирается случайный элемент, массив делится на части, где элементы больше, меньше или равны
# выбранному элементу. Нам известно сколько элементов у нас должно оказаться меньше медианы. Если длина массива с меньшми
# элементами большее этого числа, значит продолжать искать нужно в нем, если меньше него, но больше при добавлении
# длины массива с равными элементами - значит мы нашли нужную медиану, а иначе искать нужно в массиве с большими
# элементами. Причем в нем мы ищем уже не m чисел, а из m вычитаем длину массива с меньшими и равными элементами.


# def default_mediana(array, k):
#     return sorted(array)[k]
#
# def test():
#     m = 20
#     test_array = [random.randint(0, 49) for _ in range(2 * m + 1)]
#     for _ in range(100):
#         if(default_mediana(test_array, len(test_array) // 2) == mediana(test_array, len(test_array) // 2)):
#             print("Тест пройден")
#         else:
#             print("Ошибка")
#
# test()

# Тест написан с помощью сортировки встроенной функцией и поиска медианы. Тест пройден в 100% случаев.
