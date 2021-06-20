"""
the price of the house is 1000000.
if the buyer has good credit we have to give 10% discount
     otherwise
we have to give them 20% discount.
print the  payment done?
"""
discount_ten_percent = 10*1000000/100
discount_twenty_percent = 20*1000000/100
good_bad_credit = True
if good_bad_credit:
    print(f'The total down payment after 10 percent is { 1000000-discount_ten_percent}')
else:
    print(f'the total down payment after discount of 20 percent is {1000000-discount_twenty_percent} ')