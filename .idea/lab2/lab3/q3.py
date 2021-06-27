"""
3. write a function called shownumbers that takes a parameter called limit.
it should print all the numbers between 0 and limit with a label to identify
the even and odd numbers."""
def shownumbers (l):

   for i in range (1,l+1,1):
        if i %2==0:
          print(i, end= " " )
          print ('even')
        else:
            print(i,end=" ")
            print('odd')


print(shownumbers(20))








