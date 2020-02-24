import random
import sys

from introcs.stdlib import stdio

range_num = int(sys.argv[1])

random_nums = []
for i in range(range_num):
    random_nums.append(random.random())

avg = sum(random_nums) / len(random_nums)

stdio.writeln(
    f"avg = {avg}, min = {min(random_nums)}, max = {max(random_nums)}"
)
