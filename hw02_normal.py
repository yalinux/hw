#====================== 1 =============================
import math

list1 = [2 , -5, 8, 9, -25, 25, 4]
list2 = []

for item in list1:
    if item > 0 and (math.sqrt(item))%1 == 0:
            list2.append(int(math.sqrt(item)))
print(list2)

#====================== 2 =============================
date_now = '31.12.2013'
number = { '01':'первое', '02':'второе', '03':'третье', '04':'четвёртое', '05':'пятое', '06':'шестое', '07':'седьмое', '08':'восьмое', '09':'девятое', '10':'десятое', 
           '11':'одинадцатое', '12':'двенадцатое', '13':'тринадцатое', '14':'четырнадцатое', '15':'пятнадцатое', '16':'шестнадцатое', '17':'семнадцатое', '18':'восемнадцатое', '19':'девятнадцатое', '20':'двадцатое',
           '21':'двадцать первое', '22':'двадцать второе', '23':'двадцать третье', '24':'двадцать четвертое', '25':'двадцать пятое', '26':'двадцать шестое', '27':'двадцать седьмое', '28':'двадцать восьмое', '29':'двадцать девятое', '30':'тридцатое',
           '31':'тридцать первое'}
month = {'01':'января', '02':'февраля', '03':'марта', '04':'апреля', '05':'мая', '06':'июня', '07':'июля', '08':'августа', '09':'сентября', '10':'октября', '11':'ноября', '12':'декабря'}

date = []
date = (date_now.split('.'))
print(number[date[0]], month[date[1]], date[2], 'года')

#====================== 3 =============================
import random
n = int(input("Введите количество элементов: "))
list_r = []
i = 0
for i in range(n):
    list_r.append(random.randint(-100, 100))
print(list_r)

#===================== 4 =============================
lst1 = [1, 2, 4, 5, 6, 2, 5, 2]
lsta = list(set(lst1))

print(lsta)
lstb = []
for i in lst1:
    if lst1.count(i) == 1:
            lstb.append(i)
print(lstb)
