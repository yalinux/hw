


list_fruit = ["яблоко", "банан", "киви", "арбуз"]
i = 0
for f in list_fruit:
    print("{0}. {1:>6}".format(i+1, f))
    i+=1

list1 = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [9, 2, 4, 6, 8, 10, 3]
list3= []
for item in set(list1).difference(list2):
    list3.append(item)
list1 = list3
print(list1)

list1=[1,3,4,3,5,6,2,4,7,8,9,10]
list2=[]
for item in list1:
    if item%2 == 0:
        list2.append(item/4)
    else:
        list2.append(item*2)
print(list2)





