import re
import secrets
import string
from getpass import getpass
import sys

try:
    with open('common_pass.txt', 'r') as f:
        common_passwords = {line.strip() for line in f}
except FileNotFoundError:
    print("Error: common_pass.txt is required")
    sys.exit(1)

try:
    with open('breached_pass.txt', 'r') as f:
        breached_passwords = {line.strip() for line in f}
except FileNotFoundError:
    print("Error: breached_pass.txt is required")
    sys.exit(1)

print('Password Strength Checker')
mode = input("Choose: (1) Check password (2) Generate a random password: ")

if mode == '1':
    password = input('Enter your password here: ')
    lng_error = len(password) < 8
    digit_error   = re.search(r"\d", password) is None
    upper_error = re.search(r"[A-Z]", password) is None
    lower_error = re.search(r"[a-z]", password) is None
    special_error = re.search(r"[!#\$%&'\(\)\*\+,\-\./:;<=>\?@\[\\\]\^_`\{\|\}~]", password) is None

    is_strong = not any([lng_error, digit_error, upper_error, lower_error, special_error])
    if is_strong:
        print('Your password meets all the security standards')
        is_common = False
        try:
            with open('common_pass.txt', 'r') as f:
                common_passwords = [line.strip() for line in f]
                if password in common_passwords:
                    is_common = True
        except FileNotFoundError:
            print('Warning: common_pass.txt not found. Skipping blacklist check')
            sys.exit(1)
        if is_common:
            print("Error: Your password meets standards but is too common")
        else:
            print("Your password isn't common and can be used")

    if is_strong:
        is_breached= False
        try:
            with open('breached_pass.txt', 'r') as f:
                breached_passwords = [line.strip() for line in f]
                if password in breached_passwords:
                    is_breached = True
        except FileNotFoundError:
            print('Warning: breached_pass.txt not found, Skipping blacklist check')
            sys.exit(1)
        
        if is_breached:
                print('Error: your password has been breached, Please consider changing it ASAP')

        else:
            print('Your password is not been breached and is safe to use')

    else:
          print('Your password does not meet the following security requirements:')
    if lng_error:
        print('Must have atleast 8 characters.')
    if digit_error:
        print('Must have atleast one digit.')
    if upper_error:
        print('Must have atleast one uppercase letter.')
    if lower_error:
        print('Must have atleast one lowercase letter.')
    if special_error:
        print('Must have atleast one special character.')
  

if mode == '2':
    length= int(input('Please specify the desired length of your password: '))
    alphabet = string.ascii_letters + string.digits + string.punctuation
    random_pass = ''.join(secrets.choice(alphabet) for _ in range(length))
    print ('Your randomly generated password is:', random_pass)
    