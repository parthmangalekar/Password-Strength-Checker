import re

print('Password Strength Checker')
password = input('Enter your password here: ')
lng_error =len(password) < 8
upper_error = re.search(r"[A-Z]", password is None)
lower_error = re.search(r"[a-z]", password is None)
special_error = re.search(r"[!]")
print(password)