import os

def valid_neighbors(grid, visited, r, c):
    rows = len(grid)
    cols = len(grid[0])
    neighbors = 0
    valid_dirs = (-1, 0, 1)

    for dr in valid_dirs:
        for dc in valid_dirs:
            if dr == 0 and dc == 0:
                continue

            r2 = r + dr
            c2 = c + dc

            if 0 <= r2 < rows and 0 <= c2 < cols and grid[r2][c2] == "@" and (r2, c2) not in visited:
                neighbors += 1

            if neighbors >= 4:
                return False

    return True

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]
    total = 0
    rows = len(lines)
    cols = len(lines[0])
    removed = set()

    while True:
        tp_removed = 0
        
        for row in range(rows):
            for col in range(cols):
                if lines[row][col] == "." or (row, col) in removed:
                    continue
            
                if valid_neighbors(lines, removed, row, col):
                    removed.add((row, col))
                    tp_removed += 1

        if tp_removed == 0:
            break

        total += tp_removed

    print(total)
