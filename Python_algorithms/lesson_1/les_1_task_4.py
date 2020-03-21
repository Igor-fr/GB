#4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
a = input("Введите первый символ: ")
b = input("Введите второй символ: ")

first = ord('a') - 1 # -1 чтобы буква а была первой, а не нулевой
position_a = ord(a) - first
position_b = ord(b) - first
count_letter = position_b - position_a - 1

print(position_a, position_b, count_letter)