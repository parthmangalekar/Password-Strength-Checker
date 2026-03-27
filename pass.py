import re
import secrets
import string
from getpass import getpass
import sys
import requests
import hashlib

def check_password_breach(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Warning: Could not check breach database.")
        return 0

    hashes = (line.split(':') for line in response.text.splitlines())
    
    for h, count in hashes:
        if h == suffix:
            return int(count)
            
    return 0

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
         count = check_password_breach(password)

        if count:
            print(f"⚠️ Your password was found {count} times in data breaches. Change it ASAP!")
        else:
             print("✅ Your password was NOT found in known breaches.")
   
    


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
    length= int(input('Please specify your desired password length: '))
    alphabet = string.ascii_letters + string.digits + string.punctuation
    random_pass = ''.join(secrets.choice(alphabet) for _ in range(length))
    print ('Your randomly generated password is:', random_pass)
    