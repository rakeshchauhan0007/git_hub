"""

  If name is less than 3 characters long- name must be at least 3 characters
  otherwise if it's more than 50 characters - name must be maximum of 50 characters
  otherwise - name looks good!
"""
name = input('name :')

if len(name)<50 and len(name)>3:
    print('name is good')
else:
    print('name must be maximum 50 and minimum 3')





