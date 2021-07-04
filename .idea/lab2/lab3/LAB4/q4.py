"""
4.write a python program to construt the pattern using the nested loop.

"""


x="*"
y=(4,3,2,1)

for a in range(0,6,1):
     for b in range(a):
          print("*",end="")
     print('')
for d in range(4,0,-1):
    for e in range(d):
        print("*", end="")
    print('')