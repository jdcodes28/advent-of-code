import os
import re

with open("input.txt") as f:
    lines = [list(filter(None, re.split(r"\s", line.strip()))) for line in f]
    operators = lines.pop()
    total = 0

    for col in range(len(operators)):
        ct = 1 if operators[col] == "*" else 0

        for row in range(len(lines)):
            match operators[col]:
                case "+":
                    ct += int(lines[row][col])
                case "*":
                    ct *= int(lines[row][col])

        total += ct

    print(total)
