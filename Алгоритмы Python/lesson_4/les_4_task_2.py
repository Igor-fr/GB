# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого
# числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

# Преобразуем решето Эратосфена следующим образом: ищем число среди n чисел, если не находим, то увеличиваем решето
# еще на n чисел и так далее.

import cProfile


def sieve_1(n):
    sieve = list(range(n))
    sieve[1] = 0
    while True:
        counter = 0
        length = len(sieve)
        sieve += list(range(length, length + n))
        for i in range(2, length):
            if sieve[i] != 0:
                j = i + i
                while j < length + n:
                    sieve[j] = 0
                    j += i
        for i in sieve:
            if i != 0:
                counter += 1
                if counter == n:
                    return i

# Другой вариан решета - заведомо увеличить его размеры так, чтобы искомое число точно попало в решето.
# В качестве такой зависимости можно использовать n ** 1.5, она будет расширять массив больше, чем это необходимо
# особенно при больших n, но нужно проверть гипотезу о большей эффективности, чем в первом предложенном методе
def sieve_2(n):
    m = 30 if n < 10 else int(n**1.5)
    sieve = [i for i in range(m)]
    sieve[1] = 0
    spam = 0
    num = 0
    for i in range(2, m):
        if sieve[i] != 0:
            j = i * 2
            spam += 1
            if spam == n:
                return sieve[i]
            while j < m:
                sieve[j] = 0
                j += i


# Классический способ проверки числа на простоту
def prime(n):
    counter = 0
    i = 2
    while True:
        for k in range(2, i):
            if i % k == 0:
                break
        else:
            counter += 1
            if counter == n:
                return i
        i += 1


# print(prime(29))
# print(sieve_1(29))
# print(sieve_2(29))

# cProfile.run('sieve_1(10)')
# cProfile.run('sieve_1(100)')
# cProfile.run('sieve_1(1000)')
#
#  6 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:16(sieve_1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          9 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 les_4_task_2.py:16(sieve_1)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          11 function calls in 0.015 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#         1    0.015    0.015    0.015    0.015 les_4_task_2.py:16(sieve_1)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#         7    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('sieve_2(10)')
# cProfile.run('sieve_2(100)')
# cProfile.run('sieve_2(1000)')
#
#  5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:38(sieve_2)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:40(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          5 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:38(sieve_2)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:40(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          5 function calls in 0.011 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#         1    0.009    0.009    0.011    0.011 les_4_task_2.py:38(sieve_2)
#         1    0.002    0.002    0.002    0.002 les_4_task_2.py:40(<listcomp>)
#         1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('prime(10)')
# cProfile.run('prime(100)')
# cProfile.run('prime(1000)')
#
#   4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_task_2.py:56(prime)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 les_4_task_2.py:56(prime)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#          4 function calls in 0.316 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.316    0.316 <string>:1(<module>)
#         1    0.316    0.316    0.316    0.316 les_4_task_2.py:56(prime)
#         1    0.000    0.000    0.316    0.316 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Проверим первый метод на скорость работы, будем изменять порядковый номер простого числа на 10, 100 и 1000:
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_1(10)"
# 1000 loops, best of 5: 13.2 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_1(100)"
# 1000 loops, best of 5: 679 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_1(1000)"
# 1000 loops, best of 5: 14.4 msec per loop

# Аппроксимация полученных значений показывает близость к полиному:
# O(n) = 0.0079*n**2+6.5258*n−52.8507
# Таким образом, сложность первого алгоритма O(n**2)


# Проверим второй метод на скорость работы, будем изменять порядковый номер простого числа на 10, 100 и 1000:
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_2(10)"
# 1000 loops, best of 5: 8.01 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_2(100)"
# 1000 loops, best of 5: 279 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_2(1000)"
# 1000 loops, best of 5: 9.88 msec per loop
# y=0.0077x2+2.1602x−14.3659

# Аппроксимация полученных значений показывает близость к полиному:
# O(n) = 0.0077*n**2+2.1602*n−14.3659
# Таким образом, сложность второго алгоритма также O(n**2), только время работы всегда меньше приблизительно в 1.5 раза
# и эта зависимость сохраняется даже с существенным возрастанием n.


# Проверим третий метод на скорость работы, будем изменять порядковый номер простого числа на 10, 100 и 1000:
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(10)"
# 1000 loops, best of 5: 18.6 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(100)"
# 1000 loops, best of 5: 1.65 msec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(1000)"
# 1000 loops, best of 5: 285 msec per loop

# Аппроксимация полученных значений показывает близость к полиному:
# O(n)=0.2997**n*2-14.8407*n+137.0370

# Проверим третий метод на более густой сетке значений от 1 до 350:
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(1)"
# 1000 loops, best of 5: 501 nsec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(10)"
# 1000 loops, best of 5: 18.6 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(50)"
# 1000 loops, best of 5: 376 usec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(100)"
# 1000 loops, best of 5: 1.71 msec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(150)"
# 1000 loops, best of 5: 4.08 msec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(200)"
# 1000 loops, best of 5: 7.88 msec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(250)"
# 1000 loops, best of 5: 13 msec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(300)"
# 1000 loops, best of 5: 19.7 msec per loop
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(350)"
# 1000 loops, best of 5: 27.9 msec per loop

# Аппроксимация полученных значений показывает близость к полиному:
# O(n)=0.0002*n**3+0.1671*n**2−2.1076*n+30.4249
# Проверка на аналогичной сетке первых двух функций дает по прежнему сложность O(n**2)
# Таким образом, можно заключить что сложность первых двух алгоритмов O(n**2), сложность третьего алгоритма
# при небольших значениях приближается к O(n**3), но в целом на различных значениях
# лучше описывается O(n**2), хоть и время работы значительно резче возрастает, в сравнении с первым и вторым методами

# Анализ результатов, полученных от cProfile показывает аналогичные результаты. Предложенная оптимизация, реализованная
# во втором методе, приводит к сокращению времени работы и сокращению количества вызовов к функции определения длины,
# а третий метод классического поиска показывает куда более резкое возрастание времени работы при увеличении n,
# чем любые вариации решета Эратосфена.