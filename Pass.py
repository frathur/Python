Username = input("Enter your name: ")
password = input("Enter your password: ")
password_length = len(password)
while password_length < 8:
    print("Password should contain 8 or more characters.\n")
    password=input("Enter another password with required length: ")
    if len(password) >= 8:
        break
print(f'{Username} your password is ' ,f'*'*len(password),f'of length {len(password)}')