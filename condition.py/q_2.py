"""
if the temperature is greater then 30, its a hot day otherwise
if its less then 10: its a cold day;
otherwise its neither hot not cold

"""
temperature = int(input('temperature:'))
cold_day = 10 > temperature
hot_day  = 30< temperature

if cold_day:
    print(f' its a old day')
elif hot_day:
    print(f'its a hot day')
else:
    print(f'its neither hot nor cold')