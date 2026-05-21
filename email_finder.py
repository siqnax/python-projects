
#Using Regular Expressions
import re

print(' Registration Form '.center(40, '*'))
print('Enter the email addresses of your fellow student member(s) and professor(s)')

try:
    num_of_emails = int(input('How many emails are you entering: '))

    email = []                          # List to store user inputs
    compiled_email = ''                 # Variable to store email list converted to string

    for i in range(num_of_emails):
        user_input = input('Email ' + str(i + 1) + ' : ')
        email.append(user_input)        # Add user inputs to list

    compiled_email = ', '.join(email)   # converting list to string, because only allows strings

    # Regex match patterns
    student_email_regex = re.compile(r'\w+@student\.college\.edu')
    prof_email_regex = re.compile(r'\w+@prof\.college\.edu')

    student_match = student_email_regex.findall(compiled_email)
    prof_match = prof_email_regex.findall(compiled_email)

    num_of_student_emails = len(student_match)
    num_of_prof_emails = len(prof_match)

    print('\nNumber of emails entered: ', num_of_emails)
    print('You inputted ' + str(num_of_prof_emails) + ' professors emails')
    print('You inputted ' + str(num_of_student_emails) + ' students emails')

except ValueError:
    print('Invalid input. Enter an integer.')


