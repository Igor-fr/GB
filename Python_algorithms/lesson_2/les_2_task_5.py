#5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
#Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

row = ""
i = 0
for char_code in range (32,128):
    row += f"\t{char_code}-{chr(char_code)} "
    i += 1
    if(i == 10):
        row += '\n'
        i = 0
print(row)