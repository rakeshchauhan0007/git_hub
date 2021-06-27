"""
7.write a python function that accepts a string
and calculate the number of upper case letters and lower case letters
"""
string = input('string:')
for i in string :
    if i == i.lower() :
     lower= len(string)
     print(lower)
      
    elif i==i.upper() :
       upper = len(string)
       print(upper)

