import os

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    lines = f.readlines()
    ranges = []

    for line in lines:
        line = line.strip()

        if not line:
            break

        start, end = line.split("-")
        start, end = int(start), int(end)
        ranges.append((start, end))

    ranges.sort()
    count = 0
    min_so_far, max_so_far = ranges[0]

    for start, end in ranges:
        if start > max_so_far:
            count += max_so_far - min_so_far + 1
            min_so_far = start

        max_so_far = max(max_so_far, end)

    print(count + (max_so_far - min_so_far + 1))
