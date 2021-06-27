"""
9. Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
Hint: • a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
• a year is always a leap year if its number is exactly divisible by 400
"""
year_check= ""
while year_check=="":

 input_year = int(input('year to check:'))
 if input_year%4==0:
  print(f'{input_year} is a leap year')



 else:
  print(f'{input_year } is not  leap year')
