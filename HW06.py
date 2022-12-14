# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.
# print('How many elements in list?:')
# a = int(input())
# array = [round(((1 + 1/i)**i), 2) for i in range(1, a + 1)]   #  тест List Comprehension
# print(array)
# def sum(col):
#     summa = 0
#     for i in range(len(col)):
#         summa = summa + col[i]
#     return summa
# print(f'Sum for elements = {sum(array)}')


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму четных элементов списка.
# Все четные элементы возвести в куб. (поменял условие задачи чтобы потестить filter и map)
# print('How many elements:')
# n = int(input())
# numbers = [i for i in range(1, n + 1)]
# print(numbers)
# res = list(filter(lambda x: not x % 2, numbers))  # через фильтер нахожу четные элементы и сохраняю их в новый список
# print(res)
# def sum(col):
#     sum = 0
#     for i in range(len(col)):
#         sum += col[i]
#     return(sum)
# print(f'Sum for even elements = {sum(res)}')
# res = list(map(lambda x: x ** 3, res))            # через map каждый элемент возвожу в куб
# print(f'List with elements in 3rd pow = {res}')


# Задан список пользователей, создать пронумерованный список. (просто тестил enumerate)
# users = ['Albert', 'Anton', 'Ivan', 'Oleg']
# spisok = list(enumerate(users))
# print(spisok)