import os

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    ranges = f.readline().strip()
    total = 0

    for r in ranges.split(","):
        start, end = r.split("-")
        sl = len(start)
        el = len(end)

        if sl == el and sl % 2 == 1:
            continue

        start = int(start)
        end = int(end)

        for i in range(start, end + 1):
            i_str = str(i)

            if len(i_str) % 2 == 1:
                continue

            l = len(i_str) // 2
            repeats = True

            for j in range(l):
                if i_str[j] != i_str[j + l]:
                    repeats = False
                    break

            if repeats:
                total += i

    print(total) 
