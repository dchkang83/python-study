# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
#
# counter = {}
#
# for char in message:
#     # print(char)
#     counter[char] = counter.setdefault(char, 0) + 1
#
# print(counter)


import random

counter = {}
for i in range(10000):
    random_key = random.randint(1, 6)

    if random_key in range(1, 6):
        counter[random_key] = counter.setdefault(random_key, 0) + 1

print(counter)
