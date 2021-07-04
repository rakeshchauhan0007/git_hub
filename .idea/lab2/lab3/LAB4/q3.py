"""
3.guess the number between 0 to 9.
"""
guess_limit=3
right_guess= 7
for i in range(1,4,1):
    guess= int(input('guess the number:'))
    if guess==right_guess:
        print('well guessed')
        break
else:
 print('you have lost')