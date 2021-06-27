"""
4. Given three integers, print the smallest one. (Three integers should be user input)
"""
first_num=int(input('first integer:'))
second_num=int(input('second integer:'))
third_num=int(input('third integer:'))
if first_num>third_num and second_num>third_num:
    print(f'{third_num} is the smallest one')
elif second_num >first_num and third_num>first_num:
    print(f'{first_num} is the smallest number')
elif first_num>second_num and third_num>second_num:
    print(f'{second_num } is the smallest number')