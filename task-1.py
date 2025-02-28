# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'
print(st)

number = ''

for i in st:
    if i == ' ' or i.isalpha():
        continue
    elif i.isdigit():
        number += i


newStringNum = ','.join(number)
print(newStringNum)


# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st1 = 'as 23 fdfdg544 34'
print(st1)

number1 = ''

for j in st1:
    if j.isalpha():
       continue
    elif j.isdigit() or j == ' ':
        number1 += j


number2 = number1.lstrip()
number2 = number2.replace(' ', ', ')
print(number2)



