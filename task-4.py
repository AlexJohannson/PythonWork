# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]

list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

#   - знайти мін число
def minNum (list):
    minNum = min(list)
    return minNum

listMin = minNum(list)
print(listMin)
print('---------------------')


#   - видалити усі дублікати
listSet = []

for item in list:
    if item not in listSet:
        listSet.append(item)

print(listSet)
print('-----------------------')


#   - замінити кожне 4-те значення на 'X'
for i in range(3, len(list), 4):
    list[i] = 'X'

print(list)
print('-----------------------')



# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square (num):
    for i in range(num):
        if i == 0 or i == num - 1:
            print('*' * num)
        else:
            print('*' + ' ' * (num - 2) + '*')

square(10)
print('----------------------------')



# 3) вывести табличку множення за допомогою цикла while
def mulWhile ():

    i = 1
    while i <= 6:
        j = 1
        while j <= 6:
            print(f'{i} * {j} = {i * j}')
            j += 1
        i += 1
        print()

mulWhile()
print('--------------------------')



# 4) переробити це завдання під меню
def mulWhileMenu ():
    i =1
    while i <= 5:
        j = 1
        while j <= 5:
            print(f'{i} x {j} = {i * j}')
            j += 1
        i += 1
        print()


def menu ():
    while True:
        print('Menu')
        print('1. Show table')
        print('2. Exit')

        value = input('Choose action 1 or 2:')
        if value == '1':
            mulWhileMenu()
        elif value == '2':
            print('Goodbye')
            break
        else:
            print('Invalid input')

menu()
