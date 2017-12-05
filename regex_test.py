import re


# search 함수
def fn_test():
    phonenum_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phonenum_regex.search('My number is 415-555-4242.')
    print(mo)
    print(type(mo))
    print('Phone number found: ' + mo.group())


# group 함수
def fn_group():
    phonenum_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = phonenum_regex.search('My number is 415-555-4242.')
    print(mo)
    print(mo.groups())
    print(mo.group(1))

    area_code, main_number = mo.groups()
    print(area_code)
    print(main_number)


# has group
def fn_has_group():
    phonenum_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
    mo = phonenum_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
    # [('415', '555', '9999'), ('212', '555', '0000')]

    print(mo)


def test():
    phonenum_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = phonenum_regex.search('My number is 415-555-4242.')
    print(mo)
    print(mo.group())
    print(type(mo))
    print(mo.group(1))


def main():
    test()


main()
