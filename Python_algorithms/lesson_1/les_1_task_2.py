#2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
#проходящей через эти точки.

x1 = int(input("Введите координату Х первой точки: "))
y1 = int(input("Введите координату Y первой точки: "))
x2 = int(input("Введите координату X второй точки: "))
y2 = int(input("Введите координату Y второй точки: "))

if (x1 == x2):
    print("Уравнение вида y = kx + b получить невозможно.")
else:
    k = (y2 - y1)/(x2-x1)
    b = y1 - k*x1
    print(f"Уравнение прямой y = {k}x + {b}.")
