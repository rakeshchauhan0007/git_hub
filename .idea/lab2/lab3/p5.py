"""
5.write the function called show stars(rows).
if rows is 5, it should print thefollowing.
*
**
***
****
*****
"""
def show_stars(n):
 for i in range (1,n+1):
     rows=i*"*"
     print(rows)



print(show_stars(5))
