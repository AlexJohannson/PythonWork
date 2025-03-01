# function

# - створити функцію яка виводить ліст

def listD (listNum):
    print(listNum)

listNum =[1, 2, 3, 4, 5]
listD(listNum)
print('------------------------')



# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def maxNum (a, b, c):
    maxNumber = max(a, b, c)
    return maxNumber

num = maxNum(2, 34, 23)
print('Max Number is', num)
print('---------------------------')



# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def exe (*args):
    if not args:
        print('Dont find number')
    maxNum = max(args)
    minNum = min(args)
    print('Max Number is', maxNum)
    return minNum

s = exe(10, 30, 40, 34, 1, 2, 57, 12, 93)
# print('Min Number is', s)
print('--------------------------------')


# - створити функцію яка повертає найбільше число з ліста

def maxNum1 (list1):
    if not list1:
        print('List is empty')
    maxNum = max(list1)
    return maxNum

s1 = maxNum1([1, 3, 9, -2, 9, 56, 23, 54])
print('Max Number in the list is', s1)
print('---------------------------------')



# - створити функцію яка повертає найменьше число з ліста

def minNum (list2):
    if not list2:
        print('List is empty')
    minNum = min(list2)
    return minNum

s3 = minNum([2, 5, 8, -9, 45, 12, -11, 76])
print('Min Number in the list is', s3)
print('--------------------------------')



# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sumNum (numbers):
    total = sum(numbers)
    return total

s4 = sumNum([1, 3, 5, 6, 7, 10, 23])
print('Summa of the list is' ,s4)
print('------------------------------')


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def avg (numbers):
    if len(numbers) == 0:
        return None
    total = sum(numbers) / len(numbers)
    return total

s5 = avg([2, 4, 6, 4, 9, 4, 44, 76])
print('Average of the list is', s5)