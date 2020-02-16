import sys

from introcs.stdlib import stdio

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

is_sort = (x > y > z) or (x < y < z)

stdio.writeln(f"result = {is_sort}")
