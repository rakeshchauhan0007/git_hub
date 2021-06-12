"""
10: write a python program to convert seconds to day, hours, minutes, and seconds.

"""
seconds= int(input('the number of seconds to convert:'))
minutes = seconds//60
remainder = seconds%60

hours = minutes//60
remainder_min = minutes%60

day = hours//24
remainder_hour = hours%24

print(f'{seconds} sec is equal to {day} days, {remainder_hour} hours, { remainder_min}minutes and {remainder} sec')

