def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


def cube(number):
    return number**3


def main():
    result = by_three(6)
    print(result)


main()
