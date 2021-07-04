"""
10.accept the string from the user and display only those character which are present at even index.

"""
string=  str(input('string: '))
for i in string:
    if string%2==0:
     print(i)