# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

number = int(input("Введите номер буквы в алфавите: "))
first = ord('a') - 1 #чтобы а была первой, а не нулевой
letter = chr(first + number)
print(letter)