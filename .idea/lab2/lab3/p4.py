"""
4.write a function that returns the sum of multiple of 3 and 5 between 0 and limit.for example .
if limit is 20 it should return the sum of  3 , 5 ,6,9,10,12,15,18,20

"""
def sum(l):
    sum= (0)
    for i in range(1,l+1 , 1):
        if i % 3==0 or i % 5==0:
         sum= i+sum
    return sum


limit = int(input('l:'))

print(sum(limit))