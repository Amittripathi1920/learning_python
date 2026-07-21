import random

print('''**********************************************************************
        Welcome to Password Generator    
**********************************************************************''')

ui_password_length = int(input("How many letters would you want in your PASSWORD : "))
ui_symbols_length = int(input("How many symbols would you like in the PASSWORD : "))
ui_numbers_length = int(input("How many Numbers would you want? : "))

# Letters: a-z and A-Z
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

# Numbers: 0-9
numbers = ['0','1','2','3','4','5','6','7','8','9']

# Symbols: commonly allowed in passwords
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

password = ''
select_letters = ui_password_length - (ui_symbols_length + ui_numbers_length)

if ( ui_password_length >= ui_symbols_length or ui_password_length >= ui_numbers_length ) and ui_password_length >= ui_symbols_length + ui_numbers_length:
    for i in range(1,select_letters+1):
        password += letters[random.randint(0,51)]
    for i in range(1,ui_numbers_length+1):
        password += numbers[random.randint(0,9)]
    for i in range(1, ui_symbols_length+1):
        password += symbols[random.randint(0,9)]


password_final = "".join(random.sample(password, len(password)))

print(f"---------------------------------------\nYour Final Password is : {password_final}\n---------------------------------------\n")