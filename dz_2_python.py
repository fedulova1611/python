#1 Создать 2 переменных типа String с разными значениями
a, b = "Hello" , "Tanya"

#2 Создать 4 переменных типа Integer с разными значениями
c, d, e, f = 6, 4, 10, 10

#3 Создать 3 переменных типа Float с разными значениями
g, h, j = 3.2, 5.5, 6.6

#4 Реализовать 15 варианта сравнения int переменных с операторами >, <, >=, <=, !=.
# Pезультаты вывести в консоль.

print(c>d), print(c<d), print(c>=d), print(c<=d), print(c!=d)
print(e>f), print(e<f), print(e>=f), print(e<=f), print(e!=f)
print(c>e), print(c<e), print(c>=e), print(c<=e), print(c!=e)

#5 Реализовать 9 вариантов сравнения Float переменных с операторами >, <, >=, <=, !=.
# Pезультаты вывести в консоль.
print(g>h), print(g<h), print(g>=h)
print(h>=j), print(h<=j), print(h!=j)
print(g>j), print(g<j), print(g!=j)

#6Реализовать 10 вариантов сравнения int переменных с операторами >, <, >=, <=, != и
# условными выражениями (end, or, not). Pезультаты вывести в консоль.
result_1 = c>d and c>f
print("result_1 = ", result_1)
result_2 = c<d and c>f
print("result_2 = ", result_2)
result_3 = c>d or c<f
print("result_3 = ", result_3)
result_4 = e==f or e>f
print("result_4 = ", result_4)
result_5 = e!=f or e<f
print("result_5 = ", result_5)
result_6 = e!=f and e<f
print("result_6 = ", result_6)
result_7 = not (e > f)
print("result_7 = ", result_7)
result_8 = not e!=f
print("result_8 = ", result_8)
result_9 = e>f or e<f
print("result_9 = ", result_9)
result_10 = e>=f or e<f
print("result_10 = ", result_10)

#7Сделать скрипт используя функцию input().
number = input("Введите число  ")
number = int (number)
if number>30:
    print("Вы ввели число ", number, "которое больше 30")
elif number == 30:
    print("Вы ввели число ", number, "которое равно 30")
else:
    print("Вы ввели число ", number, "которое меньше 30")

#8 Сделать скрипт используя функцию input().
import random
number = input("Введите число  ")
number = int (number)
p = (random.randint(1,100))
print("Случайно сгенерированное число = ", p)

if number> p:
    print("Вы ввели число ", number, "которое больше сгененированного числа")
elif number == p:
    print("Вы ввели число ", number, "которое равно сгенерированному числу")
else:
    print("Вы ввели число ", number, 'которое меньше сгенерированного числа')

#9 Сделать скрипт используя функцию input() c двумя рандомными числами
import random
number = input("Введите число  ")
number = int (number)
p_1 = (random.randint(1,100))
p_2 = (random.randint(1,100))
print("Первое случайно сгенерированное число = ", p_1)
print("Второе случайно сгенерированное число = ", p_2)
if p_1 > p_2:
    n=p_1
    if number > n:
        print("Вы ввели число ", number, "которое больше сгенерированного числа")
    elif number == n:
        print("Вы ввели число ", number, "которое равно сгенерированному числу")
    else:
        print("Вы ввели число ", number, 'которое меньше сгенерированного числа')
elif p_1 < p_2:
    n=p_2
    if number > n:
        print("Вы ввели число ", number, "которое больше сгенерированного числа")
    elif number == n:
        print("Вы ввели число ", number, "которое равно сгенерированному числу")
    else:
        print("Вы ввели число ", number, 'которое меньше сгенерированного числа')
else:
    n=p_1=p_2
    if number > n:
        print("Вы ввели число ", number, "которое больше сгенерированного числа")
    elif number == n:
        print("Вы ввели число ", number, "которое равно сгенерированному числу")
    else:
        print("Вы ввели число ", number, 'которое меньше сгенерированного числа')