password = input('Enter the password: ')
password_repeat = input('Repeat please: ')

if password.lower() == password_repeat.lower():
    if password == password_repeat:
        print("Thank you")
    else:
        print("They must be in the same case")
else:
    print("Incorrect")