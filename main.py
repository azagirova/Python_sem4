# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в 
#порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# from random import randint
# n = set(randint(1, 20) 
#     for i in range(int(input("Введите количество элементов первого множества: "))))
# m = set(randint(1, 20)
#     for i in range(int(input("Введите количествово элементов второго множества: "))))
# n1 = set(input("Введите элементы первого массива: " ))
# m1 = set(input("Введите элементы второго массива: " ))
# sort = sorted(n1.intersection(m1))
# print(*sort)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только 
# по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло 
# ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и 
# нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает 
# ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь 
# перед некоторым кустом заданной во входном файле грядки.

# from random import randint
# n = list(randint(1, 20)
#     for i in range(int(input("Введите количество кустов: "))))
# print(n)
# i = int(input("Введите номер куста: "))
# ai = 0
# if ai == 1:
#     max = n[0] + n[1] + n[-1]
# elif ai == len(n):
#     max = n[-2] + n[-1] + n[0]
# else:
#     max = n[ai-1] + n[ai-2] + n[ai]
# print(max)