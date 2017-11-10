colors = ['red', 'yellow', 'blue', 'green', 'orange']

# for item in colors:
#     print(item)


# wish_travel_city = {
#     'aa': '111',
#     'bb': '222',
#     'cc': '333',
# }
#
# for key in wish_travel_city:
#     print(key)
#
# for key in wish_travel_city.keys():
#     print(key)
#
# for value in wish_travel_city.values():
#     print(value)
#
# for key, value in wish_travel_city.items():
#     print(key, ' : ', value)

# addresses = {
#     '1': {'name': 'hone kildong', 'email': 'hone@mail.com', 'hp_num': '010-2343-9870'},
#     '2': {'name': 'lee soosin', 'email': 'lee@mail.com', 'hp_num': '010-3333-5555'},
#     '3': {'name': 'jang youngsil', 'email': 'jang@mail.com', 'hp_num': '010-7777-1234'},
#     '4': {'name': 'king sejong', 'email': 'king@mail.com', 'hp_num': '010-8888-0987'},
# }
#
# for key in addresses:
#     my_dict = addresses[key]
#     print(my_dict)

# random module
import random

counter = {}

for i in range(10000):
    print(i, ' : ', random.randint(1, 6))


# 만번 돌려서 1~6까지 몇번 나왔는지 확인

