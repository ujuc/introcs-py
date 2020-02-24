import math

from introcs.stdlib import stdio

number = [2**x for x in range(1, 11)]

for n in number:
    stdio.write(f"{math.log2(n)}\t")
    stdio.write(f"{n}\t")
    stdio.write(f"{math.log(n, math.e)}\t")
    stdio.write(f"{math.pow(n, 2)}\t")
    stdio.write(f"{math.pow(n, 3)}\t")
    stdio.writeln(f"{math.pow(2, n)}")
