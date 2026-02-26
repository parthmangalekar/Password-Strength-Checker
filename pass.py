import re

print('Password Strength Checker')
password = input('Enter your password here: ')
lng_error =len(password) < 8

password_good = not (lng_error)
if password_good:
    print('strong pass')

else: 
    if lng_error:
        print('error')
print(password)