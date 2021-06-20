guess_num = 10
low_guess_num = 0
guess_limit = 3
while low_guess_num< guess_limit:
    guess = int(input('guess:'))
    low_guess_num = low_guess_num + 1
    if guess_num == guess :
        print('you won')
        break

else:
    print('you lost')
