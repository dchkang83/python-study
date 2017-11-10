import pyperclip

PASSWORDS = {
    'gmail': 'gmail123',
    'naver': 'naver123',
    'facebook': 'facebook123',
}


def main():
    site = input('input your site : ')

    password = PASSWORDS[site]

    if not password:
        print('not valid site')
    else:
        pyperclip.copy(password)
        print('your password is copied')


main()
