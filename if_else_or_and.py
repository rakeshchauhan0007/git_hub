income = int(input('income of the student:'))
enough_income = 20000<income
experience = int(input('years of experience:'))

work_experience_year= 2<experience

if enough_income and work_experience_year:
    print('student is eligible for the job')

elif enough_income or work_experience_year:
    print('student has to give interview')
else:
    print('student is not eligible for the job')

