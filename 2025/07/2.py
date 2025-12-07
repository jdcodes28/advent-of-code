import os

with open("input.txt") as f:
    lines = [line.strip() for line in f]
    cols = len(lines[0])
    beams = [0] * cols
    prev = [0] * cols

    for i in range(cols):
        if lines[0][i] == "S":
            beams[i] = 1
            break

    count = 0

    for row in range(2, len(lines) - 1, 2):
        for col in range(cols):
            if beams[col] > 0 and lines[row][col] == "^":
                prev[col] = beams[col]

                if col > 0:
                    beams[col - 1] += prev[col] 

                beams[col] -= prev[col]

                if col < cols - 1:
                    beams[col + 1] += prev[col]

    print(sum(beams))
