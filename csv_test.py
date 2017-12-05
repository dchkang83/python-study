import csv
import pprint

with open('D:\\python\\csv_test.csv', 'r') as file:
    reader = csv.reader(file)
    park_list = list(reader)

    # for row in reader:
    #     print(row)


# print(park_list)
pprint.pprint(park_list)
