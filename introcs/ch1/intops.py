import sys

from introcs.stdlib import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])

total = a + b
diff = a - b
prod = a * b
quot = a // b
rem = a % b
exp = a ** b

stdio.writeln(f'{str(a)} +  {str(b)} = {str(total)}')
stdio.writeln(f'{str(a)} -  {str(b)} = {str(diff)}')
stdio.writeln(f'{str(a)} *  {str(b)} = {str(prod)}')
stdio.writeln(f'{str(a)} // {str(b)} = {str(quot)}')
stdio.writeln(f'{str(a)} %  {str(b)} = {str(rem)}')
stdio.writeln(f'{str(a)} ** {str(b)} = {str(exp)}')
