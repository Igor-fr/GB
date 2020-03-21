# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел
# в диапазоне от 2 до 9. Примечание: 8 разных ответов.

# Не совсем понятно из задания - генерируется ли массив, или это всегда ряд чисел от 2 до 99
# Если генерируется, то раскоменитровать строки с 6 по 13 и закоментировать 15
# import random
#
# try:
#     c = int(input("Введите количество генерируемых чисел: "))
# except ValueError:
#     print("В следующий раз вводите только целые числа, до свидания.")
#     exit()
# first_list = [random.randint(2, 99) for _ in range(c)]

first_list = [number for number in range(2, 100)]
second_list = [number for number in range(2, 10)]
result = [0] * 8

for first_number in first_list:
    for i, second_number in enumerate(second_list):
        if first_number % second_number == 0:
            result[i] += 1

result_string = ""

for i, number in enumerate(result):
    result_string += f"{i+2} - {number}; "

print(first_list)
print(result_string)