import os

with open("test.txt") as f:
    lines = [line.strip() for line in f]
    cols = len(lines[0])
    start = -1

    for i in range(cols):
        if lines[0][i] == "S":
            start = i
            break

    beams = [False] * len(lines[0])
    beams[start] = True
    count = 0

    for line in lines:
        for col in range(cols):
            if line[col] == "^" and beams[col]:
                beams[col] = False
                count += 1

                if col > 0:
                    beams[col - 1] = True

                if col < cols - 1:
                    beams[col + 1] = True

    print(count)
