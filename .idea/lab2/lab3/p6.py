"""
6.write a python program to reverse the string
"""

def reverse_string():
 string = input('string:')
 length = len(string)
 limit_num = length * (-1) - 1
 return string[-1:limit_num:-1]


print(reverse_string())
