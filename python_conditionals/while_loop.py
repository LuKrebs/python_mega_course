password = ''
while password != 'python123':
    password = input('Enter a password: ')
    if password == 'python123':
        print("You are logged in!")
    else:
        print("Sorry, try again")