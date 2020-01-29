import random
from crunchnum import *

fixed_tuple = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
random_list = [0] * 11
for i in range(len(random_list)):
    random_list[i] = random.randint(0, 50)
random_list.sort()

print("TUPLE DATA: ", fixed_tuple)
crunch_numbers(fixed_tuple)
print()
print("RANDOM DATA: ", random_list)
crunch_numbers(random_list)
