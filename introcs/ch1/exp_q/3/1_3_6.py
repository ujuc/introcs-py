import sys

from introcs.stdlib import stdio

end_num = int(sys.argv[1])

if end_num > 1000:
    stdio.writeln("Error: out of range")
    exit(1)

for i in range(1, end_num + 1):
    if (i % 10) == 1:
        stdio.writeln(f"{i}st Hello")
    elif (i % 10) == 2:
        stdio.writeln(f"{i}nd Hello")
    elif (i % 10) == 3:
        stdio.writeln(f"{i}rd Hello")
    else:
        stdio.writeln(f"{i}th Hello")

