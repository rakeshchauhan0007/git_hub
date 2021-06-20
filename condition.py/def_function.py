def sub(x,y,z):
    x = int(input('first value:'))
    y = int(input('second value:'))
    z = int(input('third value:'))
    subtraction = x -y -z
    return  subtraction
def add(a,b,c):
    a = int(input('first value:'))
    b = int(input('second value:'))
    c = int(input('third value:'))
    addition = b + a + c
    return  addition

p = int(input('1st input:'))
q = int(input('2nd input:'))
r = int(input('3rd input:'))
sum = add(p,q,r)
print(sum)
sub = sub(1,4,3)
print(sub)