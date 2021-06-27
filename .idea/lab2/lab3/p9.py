"""
9.write a python function to check whether the passed string is palindrome or not
"""
def palindrome():
 string= input('string:')
 length = len(string)
 l = length*(-1)-1
 if string[-1:l:-1] == string[0:length:1]:
  return 'it is palindrome'
 else:
   return "it is not paindrome"


print(palindrome())