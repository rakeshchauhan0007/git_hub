"""
2.write a function called fizz_buzz that takes a number:
if the number is divisible by 3 return fizz
if it is divixsible by 5 it should reurn buzz
if it is divisible by both 5 and 3 it should return fixxbuzz
otherwise it should return the same num
"""
def fizz_buzz(number):
    if number%3==0:
     return  "fizz"

    if number%5==0:
     return "buzz"

    if number%5==0 and number%3==0 :
     return "fizzbuzz"

    if number%5!=0 and number%3!=0 :
     return number

number = int(input('number:'))
print(fizz_buzz(number))
