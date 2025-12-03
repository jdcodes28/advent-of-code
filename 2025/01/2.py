import os

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    lines = f.readlines()
    count = 0
    dial = 50

    for line in lines:
        line = line.strip()
        direction = line[0]
        num = int(line[1:])
        hits = 0

        if direction == "L":
            target = dial - num
            hits = ((dial - 1) // 100) - ((target - 1) // 100)
        else:
            target = dial + num
            hits = target // 100

        count += hits
        dial = target
        dial %= 100

    print(count)
