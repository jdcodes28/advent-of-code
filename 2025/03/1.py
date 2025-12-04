import os

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]
    total = 0

    for line in lines:
        b1, b2 = 0, 0
        i1 = 0
        n = len(line)

        for i in range(n - 1):
            current_char = ord(line[i]) - ord("0")

            if current_char > b1:
                i1 = i

            b1 = max(b1, current_char)

        for i in range(i1 + 1, n):
            current_char = ord(line[i]) - ord("0")
            b2 = max(b2, current_char)

        total += (b1 * 10) + b2

    print(total)
