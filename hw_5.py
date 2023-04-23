# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def step(a, b):
#   if b == 0:
#     return 1
#   elif b == 1:
#     return a
#   elif b == 2:
#     return a ** b
#   else: 
#     return a * step(a, b-1)

# a = int(input("Input number a: "))
# b = int(input("Input number b: "))

# print(step(a, b))




# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#  Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         return sum(a ^ b, (a & b) << 1)
    
# a = int(input("Input number a: "))
# b = int(input("Input number b: "))

# print(sum(a, b))
