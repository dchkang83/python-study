def validate_password(password=''):
    if len(password) < 8:
        return False
    elif password.isalpha():
        return False
    elif password.isnumeric():
        return False
    else:
        return True



def main():
    user_password = input('input your password: ')

    if validate_password(user_password):
        print('valid password')
    else:
        print('not valid password')


main()
