import random
import my_module
#
# rand_num = random.randint(1, 10)
# print(rand_num)
# print(my_module.my_fav_number)
#
# random_float_num_0_to_1 = random.random() * 10
# print(random_float_num_0_to_1)
#
# random_float = random.uniform(1, 10)
# print(random_float)
#

rand_num = random.randint(1, 10)

if  1 <= rand_num <= 5:
    print("Heads")
elif 6 <= rand_num <= 10:
    print("Tails")

print(rand_num)