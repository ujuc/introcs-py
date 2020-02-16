import sys

from introcs.stdlib import stdio

input_num = []
input_num.append(int(sys.argv[1]))
input_num.append(int(sys.argv[2]))
input_num.append(int(sys.argv[3]))

min_num = min(input_num)
max_num = max(input_num)
input_num.remove(min_num)
input_num.remove(max_num)

stdio.writeln(f"sort: {min_num, input_num[0], max_num}")
