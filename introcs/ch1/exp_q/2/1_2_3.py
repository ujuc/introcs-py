from introcs.stdlib import stdio

a = True
b = False

stdio.writeln((not (a and b) and (a or b)) or ((a and b) or not (a or b)))
