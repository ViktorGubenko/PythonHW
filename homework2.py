# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
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


# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите целое число N: '))
# m = 1
# res_list = []
# for i in range(1, n+1):
#     m *= i
#     res_list.append(int(m))
# print(f'Набор произведений чисел от 1 до {n}:', res_list)

# 3.Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}

# n = int(input("Введите чилсо N: "))
# d = dict() # d = {}
# j=1
# for i in range(n):
#     d[j] = round((1 + 1 / j)**j, 2)
#     j += 1
# print (d)

# 4.Реализуйте алгоритм перемешивания списка.
import random

n = int(input('Введите кол-во элементов: '))
input_list = [i for i in range(n)]
result_list = input_list[:]
for i in range(n):
    index_random = random.randint(0, n - 1)
    temp = result_list[i]
    result_list[i] = result_list[index_random]
    result_list[index_random] = temp
print('Исходный список', input_list)
print('Перемешанный список', result_list)