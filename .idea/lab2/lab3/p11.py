"""
11.write a program to find the factorial of a number using function.

"""
def factorial():
   n= int(input('number to factor: '))
   fact=1
   for i in range(1,n+1):
    fact= i * fact
   return fact


print(factorial())
