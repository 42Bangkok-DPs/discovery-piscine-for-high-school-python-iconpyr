#!/usr/bin/env python3
my_list = [2, 8, 9, 48, 8, 22, -12, 2]
print(my_list)
my_list2 = []

for num in my_list:
    newnum = num
    newnum += 2
    if newnum >= 10:
        my_list2.append(newnum)

print(my_list2)
