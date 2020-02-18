import random
import sys

from introcs.stdlib import stdio

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])

bets = 0
wins = 0
for t in range(trials):
    cash = stake
    while (cash > 0) and (cash < goal):
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1

    if cash == goal:
        wins += 1

stdio.writeln(f"{100 * wins // trials}% 이김")
stdio.writeln(f"평균 베팅 수: {bets // trials}")
