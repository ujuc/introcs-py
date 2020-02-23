import random
import sys

range_num = int(sys.argv[1])

random_nums = []
for i in range(range_num):
    random_nums.append(random.random())

avg = [map()]
