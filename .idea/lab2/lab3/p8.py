"""
8.write a function that takes a number as a parameter and check the number is prime or not.

"""
def prime(num):
  for i in range(2,num,1):
    if num % i==0:
     return('it is not a prime number')
     break

  else:
     return('it is a prime number')


print(prime(189))