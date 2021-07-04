"""
7.write a python program that prints all the number from 0 to 6 except 6 and 3.
"""
num=[0,1,2,3,4,5,6]
num.remove(3)
num.remove(6)
print(num)
for i in range(0,7,1):#just for practising
    if i!=3 and i!=6:
        print(i,end="")

