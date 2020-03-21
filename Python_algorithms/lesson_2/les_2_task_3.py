#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#Например, если введено число 3486, надо вывести 6843.

number = int(input("Введите число: "))
reverse_number = ""
while number != 0:
    reverse_number += str(number % 10)
    number //= 10
reverse_number = int(reverse_number)
print(reverse_number)