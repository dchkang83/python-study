import time


def calc_prod():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 30000):
        product = product * i
    return product


def main():
    start = time.time()
    prod = calc_prod()
    end = time.time()
    print('The result is {0}'.format(len(str(prod))))
    print('Took {0} seconds to calculate.'.format(end - start))


if __name__ == '__main__':
    main()
