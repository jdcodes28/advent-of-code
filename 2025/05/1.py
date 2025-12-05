import os

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    lines = f.readlines()
    changed = False
    nums = []
    ranges = []

    for line in lines:
        line = line.strip()

        if not line:
            changed = True
            continue

        if changed:
            nums.append(int(line))
        else:
            start, end = line.split("-")
            start, end = int(start), int(end)
            ranges.append((start, end))

    ranges.sort()
    nums.sort()
    count = 0
    current_range = 0
    r = len(ranges)
    last_range = 0

    for num in nums:
        for r2 in range(current_range, r):
            last_range = r2
            start, end = ranges[r2]

            if start <= num <= end:
                count += 1
                break
            elif num < start:
                break

        current_range = last_range

    print(count)
