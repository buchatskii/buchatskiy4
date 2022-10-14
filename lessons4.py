# Задание 1
# num = int(input('Округлить число π до: '))
# π = 3.1415926535897932384626433832795
# print("Округленное число π: ",round(π, num))

# Задание 2
# num = int(input('Задайте натуральное число N: '))
# mult = []
# simpNumber = 2
# while num != 1:
#     if num % simpNumber == 0:
#         mult.append(simpNumber)
#         num = num / simpNumber
#         simpNumber = 2
#     else:
#         simpNumber += 1
# print(mult)

# Задание 3

# import random
# list = [random.randint(0, 10) for i in range(random.randint(5, 10))]
# inter = 0
# print(f"Заданный список:\n{list}")
# a = 0
# while a < len(list):
#     b = a + 1
#     while b < len(list):
#         if list[a] == list[b]:
#             del list[b]
#             inter = 1
#             b = a + 1
#         elif b == len(list)-1 and inter == 1:
#             del list[a]
#             a =- 1
#         else:
#             b += 1
#     a += 1
#     inter = 0
# print(f"Список без повторений:\n{list}")