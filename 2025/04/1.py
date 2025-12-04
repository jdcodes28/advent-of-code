import os

def valid_neighbors(grid, r, c):
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

            if 0 <= r2 < rows and 0 <= c2 < cols and grid[r2][c2] == "@":
                neighbors += 1

            if neighbors >= 4:
                return False

    return True

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]
    total = 0
    rows = len(lines)
    cols = len(lines[0])

    for row in range(rows):
        for col in range(cols):
            if lines[row][col] == ".":
                continue
            
            if valid_neighbors(lines, row, col):
                total += 1

    print(total)
