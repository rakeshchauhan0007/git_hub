"""
the price of the house is 10000000.
if the buyer has good credit we have to give 10% discount
     otherwise
we have to give them 20% discount.
print the  payment done?
"""
credit_of_buyer = int(input('the total assets the buyer has: '))
good_credit = credit_of_buyer>20000000
discount_ten_percent = 10*10000000/100
discount_twenty_percent = 20*10000000/100
if good_credit:
    print(f'The total down payment after 10 percent is { 10000000-discount_ten_percent}')
else:
    print(f'the total down payment after discount of 20 percent is {10000000-discount_twenty_percent} ')
