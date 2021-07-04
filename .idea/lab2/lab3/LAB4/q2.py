"""
2.write a python prograM TO CONVERT TEMPERATURE to  and celsius, farheinheit.
"""
celsius_ferheinheit=float(input('input celsius or fehreinheit= '))
c_f=input('if celsius to fehreinheit type f and if  fehreinheit to celsius type  c:  ')
if c_f=='c':
 celsius= (celsius_ferheinheit -32) *5/9
 print(f'{celsius}degree celsius')
else:
 ferheinheit=(celsius_ferheinheit * 9/5) + 32
 print(f'{ferheinheit} degree fehrenheit')

