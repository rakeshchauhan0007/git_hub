"""
10. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

"""
def number(first,second,third):
   return first + second + third

x=int(input('first number:'))
y=int(input('second number:'))
z= int(input('third number:'))
if x == y:
    print('summ is zero')
elif y==z:
    print('summ is zero')
else:
 print(number(x,y,z))
