
try:
    file = open('abc.txt', 'r')
    print(file)
except:
    print('ERRROR')

try:
    price = float('hello')
    print('Price =', price)
except ValueError as e:
    print('Not a number ' + str(e))


class BizException(Exception):
    pass

try:
    number = float('asfds')
    print(number)
except ValueError as e:
    raise BizException(e)
