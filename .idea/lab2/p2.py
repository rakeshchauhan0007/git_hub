"""
2. WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70%
 –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail

"""
name = input('name of the student:')
science = int(input('score obtained in science:'))
math = int(input('score obtained in math:'))
health = int(input('score obtained in health'))
english = int(input('score obtained in english:'))
total_marks = 400
marks_obtained_total= science+health+english+math
one_marks= 100/400
percentage_obtained= marks_obtained_total*one_marks
print(f' the total marks obtained by {name} out of 400 is {marks_obtained_total}')
print(f'The percentage secured by {name} is {percentage_obtained} percent')

if percentage_obtained >70:
    print(f'the {name} have secured distinction')
elif percentage_obtained<40:
    print(f'the {name} have failed the exam')
elif percentage_obtained > 40 and percentage_obtained<60:
    print(f'the {name} have passed the exam with just pass score')
elif percentage_obtained >60:
    print(f'first')
