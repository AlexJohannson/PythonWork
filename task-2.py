# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'

newList = []

for item in greeting:
    if item.isalpha():
        newList.append(item.upper())
    else:
      newList.append(item)

print(newList)



# з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

newList1 = []

for num in range(51):
    if num % 2 != 0:
        newList1.append(num**2)


print(newList1)



