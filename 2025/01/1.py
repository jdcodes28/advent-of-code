import os

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    lines = f.readlines()
    count = 0
    dial = 50

    for line in lines:
        line = line.strip()
        direction = line[0]
        num = int(line[1:])
        dial = (dial + (-1 if direction == "L" else 1) * num) % 100

        if dial == 0:
            count += 1

    print(count)
