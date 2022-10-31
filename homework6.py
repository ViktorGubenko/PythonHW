# Задача 1. Напишите программу, которая найдёт произведение пар чисел списка.
# #Парой считаем первый и последний элемент, второй и предпоследний
# Старый код
# ent_list = [2, 3, 4, 5, 6]
# res_list = []
# for i in range ((len(ent_list)+1)//2):
#     res_list.append(ent_list[i]*ent_list[len(ent_list)-1-i])
# print(res_list)
# Новый вариант ------------------------------------------------------------------------------
lst = [1,2,4,5,5,3,7,8,9]
product = lambda x, y: x*y
lst1 = [product(lst[i], lst[len(lst)-1-i]) for i in range(len (lst)) if i<(len(lst)/2)]
print(lst1)

# Задача 2. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11
# print ('введите a:', end = ' ')
# a = list(input())
# sum = 0
# for i in range(len(a)):
#     if a[i] == '.':
#         continue
#     sum += int(a[i])
# print (sum)
# Новый вариант ------------------------------------------------------------------------------

real_num = input("Введите вещественное число:   ")

def func(x):   
    if x == "." :return 0
    return int(x)
li = list(map(func,real_num))
print("сумма цифр вещественного числа равна ",sum(li))

# Задача 3. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# def sum_odd (ent_list):
#     n = 0
#     for i in range(len(ent_list)): 
#         if i % 2 != 0:
#             n += ent_list[i]
#     print(f"Сумма равна: {n}")

# for i in range(1,len(ent_list),2):
# n += ent_list[i]

# lst = list(map(int, input("Введите числа через пробел: ").split()))
# sum_odd(lst)
# Новый вариант ------------------------------------------------------------------------------
lst = [2, 3, 5, 9, 3]
sum_odd_index(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)