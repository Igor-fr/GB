#3. Написать программу, которая генерирует в указанных пользователем границах:
#a. случайное целое число,
#b. случайное вещественное число,
#c. случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный
#символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ
#алфавита от 'a' до 'f' включительно.

import random

i1 = int(input("Введите нижнюю границу для целого числа: "))
i2 = int(input("Введите верхнюю границу для целого числа: "))
j1 = float(input("Введите нижнюю границу для вещественного числа: "))
j2 = float(input("Введите верхнюю границу для вещественного числа: "))
k1 = input("Введите первый символ в диапазоне для генерации символа: ")
k2 = input("Введите последний символ в диапазоне для генерации символа: ")

a = random.randint(i1, i2)
b = random.uniform(j1, j2)
k1 = ord(k1)
k2 = ord(k2)
c = chr(random.randint(k1, k2))

print(a, b, c)