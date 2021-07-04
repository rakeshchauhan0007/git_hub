"""
6.write a python program that counts odd and even number from the series of number.
"""
n=int(input('give any number:'))
total=0
sum=0
for i in range(1,n):
     if i%2==0:

      i=1
      sum+=i
print(f'{sum} is total numbers of even number below {n}')
if not i%2==0:
    i=1
    sum+=i
print(f'{sum} is total number of odd number below {n}')

