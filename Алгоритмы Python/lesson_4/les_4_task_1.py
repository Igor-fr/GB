# Результаты анализа сохранить в виде комментариев в файле с кодом.
# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
# трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы
# проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# Выбрано задание 4 из 3 урока, а именно:
# Определить, какое число в массиве встречается чаще всего.

import random
import timeit
import cProfile


# Вариант на основе использования массива, где каждая ячейка будет хранить частоту соответствующего числа
def find_often_number_1(start, end, size):

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

    #print(first_list)
    #print(max, max_frq)

# Вариант на основе прямого подсчета частоты встречаемости чисел и одновременного поиска максимальной частоты
def find_often_number_2(start, end, size):

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

    #print(first_list)
    #print(max, max_frq)

# Вариант с использованием словаря (логика как в певром варианте, но с использованием словаря, упрощающего
# и значительно сокращающего реализацию)
def find_often_number_3(start, end, size):

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
        if(result[item] > max_frq):
            max_frq = result[item]
            max = item

    #print(first_list)
    #print(max, max_frq)


#find_often_number_1(1, 10, 20)
#find_often_number_2(1, 10, 20)
#find_often_number_3(1, 10, 20)


# Первая функция

#cProfile.run('find_often_number_1(1,10,20)')
# 131 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1.py:21(find_often_number_1)

#cProfile.run('find_often_number_1(1,10,200)')
# 1100 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 les_4_task_1.py:21(find_often_number_1)

#cProfile.run('find_often_number_1(1,10,2000)')
# 11260 function calls in 0.010 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#         1    0.000    0.000    0.010    0.010 les_4_task_1.py:21(find_often_number_1)



# Вторая функция

# cProfile.run('find_often_number_2(1,10,20)')
# 116 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:41(find_often_number_2)

# cProfile.run('find_often_number_2(1,10,200)')
# 1130 function calls in 0.005 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.004    0.004    0.005    0.005 les_4_task_1.py:41(find_often_number_2)

# cProfile.run('find_often_number_2(1,10,2000)')
# 11223 function calls in 0.294 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.294    0.294 <string>:1(<module>)
#         1    0.287    0.287    0.294    0.294 les_4_task_1.py:41(find_often_number_2)



# Третья функция

# cProfile.run('find_often_number_3(1,10,20)')
# 136 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_1.py:61(find_often_number_3)

# cProfile.run('find_often_number_3(1,10,200)')
# 1309 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 les_4_task_1.py:61(find_often_number_3)

# cProfile.run('find_often_number_3(1,10,2000)')
# 13181 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.001    0.001    0.007    0.007 les_4_task_1.py:61(find_often_number_3)



# Проверим первый метод, будем менять длину массива, в котором происходит поиск: 20, 200 и 2000 элементов

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_1(1,10,20)"
# 1000 loops, best of 5: 41.6 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_1(1,10,200)"
# 1000 loops, best of 5: 388 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_1(1,10,2000)"
# 1000 loops, best of 5: 3.92 msec per loop


# Проверим второй метод аналогично:

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_2(1,10,20)"
# 1000 loops, best of 5: 65.3 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_2(1,10,200)"
# 1000 loops, best of 5: 2.56 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_2(1,10,2000)"
# 1000 loops, best of 5: 228 msec per loop


# Проверим третий метод аналогично:

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_3(1,10,20)"
# 1000 loops, best of 5: 44.3 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_3(1,10,200)"
# 1000 loops, best of 5: 453 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_3(1,10,2000)"
# 1000 loops, best of 5: 4.66 msec per loop

# Из полученных результатов следует, что самый быстродейственный метод - первый, то есть с использованием массива.
# Метод с использованием словаря незначительно отстает по эффективности, а метод прямого поиска значительно
# медленнее. Итак, время работы первого и третьего методов приблизительно линейно возрастает с увеличением сложности,
# время работы второго метода возрастает значительно быстрее, зависимость степенная, так как при увеличении
# в 10 раз время возросло в 40 раз, а при увеличении в 100 раз - в 3500 раз.
# Аппроксимация по полученным значениям показала, что зависимость времени работы для второго метода от размера массива
# лучше всего описывается функцией:
# O(n)=0.0563*n**2+1.4833*n+13.1313
# Таким образом сложность первого и третьего алгоритмов O(n), второго алгоритма O(n**2)
# Однако нужно заметить, что поскольку первый метод (с использованием массива) требует увеличения результирующего
# массива при увеличении диапазона значений в исходном массиве, то необходимо проверить эффективность также при
# увеличении значений start и end, ведь больший массив с частотой требует больше памяти и времени для поиска


# Проверим первый метод, будем менять диапазон значений в выборке, сдвигать end на 10, 1000, 100000:

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_1(1,10,200)"
# 1000 loops, best of 5: 440 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_1(1,1000,200)"
# 1000 loops, best of 5: 563 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_1(1,100000,200)"
# 1000 loops, best of 5: 15.1 msec per loop


# Проверим второй метод аналогично:

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_2(1,10,200)"
# 1000 loops, best of 5: 2.61 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_2(1,1000,200)"
# 1000 loops, best of 5: 2.58 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_2(1,100000,200)"
# 1000 loops, best of 5: 2.56 msec per loop


# Проверим третий метод аналогично:

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_3(1,10,200)"
# 1000 loops, best of 5: 458 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_3(1,1000,200)"
# 1000 loops, best of 5: 455 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.find_often_number_3(1,100000,200)"
# 1000 loops, best of 5: 490 usec per loop


# Как видно из проведенного анализа - время для второго и третьего методов практически не меняется при увеличении
# диапазона чисел в исходном массиве, тогда как для первого метода время увеличивается при увеличении
# в 100 раз - в 1.2 раза, при увеличении в 10000 раз - в 34 раза, зависимость линейная, O(n).

# Анализ результатов, полученных от cProfile показывает аналогичные результаты - приблизительно линейное возрастание
# времени работы первой и третьей функции, и резкое возрастатние временя для второй функции. Число вызовов всегда равно
# единице, поскольку отсутствует вложенность.

# Окончательный вывод из проведенного анализа - самым эффективным вариантом поиска является вариант, реализованный
# в третьей функции с использованием словаря. Однако необходимо заметить, что при равной длине исходного массива,
# и при этом небольшом диапазоне его возможных значений (около 10 чисел) первый вариант с использованием массива
# несколько быстрее осуществляет поиск. Причиной эффективности словаря является линейная сложность - один проход
# по исходному массиву, и один проход по полученному словарю. При использовании массива сложность алгоритма такая же,
# однако при большом количестве различных значений в исходном массиве размер результриующего массива значительно
# возрастает, чего не происходит со словарем, и время поиска в нем возрастает соответственно. Второй же метод был
# заведомо значительно медленнее, поскольку требует многократного прохождения по частям исходного массиву, что при
# его увеличении резко увеличивает время поиска.
# Cложность первого и третьего алгоритмов O(n), второго алгоритма O(n**2)

# В общем случае предпочтение всегда нужно отдавать варианту с использованием словаря.