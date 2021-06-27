"""
write a program to remove the duplicate number from the list
"""
list=[1,3,5,6,7,8,9,4,3,2,3,4,5,6,8]
list.remove(3)
list.remove(3)
num = []
list.sort()
list.reverse()


print(list)

for x in list:
    if x not in num:
        num.append(x)
print(num)