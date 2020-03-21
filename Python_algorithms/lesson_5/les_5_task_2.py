# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

HEX_DEX = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
       'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

DEX_HEX = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
       10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def hex_sum(first, second):

    first = deque(first)
    second = deque(second)
    result = deque()
    sum = 0
    spam = 0

    while first or second:
        if not first:
            sum = HEX_DEX[second.pop()] + spam
            spam = 0
        elif not second:
            sum = HEX_DEX[first.pop()] + spam
            spam = 0
        else:
            sum = HEX_DEX[first.pop()] + HEX_DEX[second.pop()] + spam
            spam = 0
        if sum > 15:
            sum -= 16
            spam = 1
        result.appendleft(DEX_HEX[sum])

    if spam:
        result.appendleft('1')

    str = ''
    for i in result:
        str += i

    return str

def hex_mul(first, second):

    count = 0
    second_temp = list(second)
    second_temp.reverse()

    for i, num in enumerate(second_temp):
        count += HEX_DEX[num] * (16**i)

    result = '0'
    for _ in range(count):
        result = hex_sum(result, first)

    return result


first = input("Введите первое число :").upper()
second = input("Введите второе число: ").upper()

print(hex_sum(first, second))
print(hex_mul(first, second))

