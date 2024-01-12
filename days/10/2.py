import os
import pprint

import sys
sys.setrecursionlimit(100000)

os.system("clear")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/10/input.txt").read().splitlines()
lines = open("days/10/example1.txt").read().splitlines()
# lines = open("days/10/example2.txt").read().splitlines()

grid = [list(x) for x in lines]

pp(grid)

top = "|7F"
right = "-J7"
bottom = "|LJ"
left = "-FL"

line, col = 0, 0
for l in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[l][c] == "S":
            line, col = l, c

pp((line, col))

counter = 0
passed_slots = {}

def get_next_tile(from_dir, l, c):
    pp(f"current pos: {(l, c)}: {grid[l][c]}")

    if (l, c) in passed_slots:
        pp(f"already passed {(l, c)}")
        return 'error'
    passed_slots[(l, c)] = True

    global counter
    counter += 1

    if from_dir == "top":
        if grid[l][c] == "|":
            return get_next_tile("top", l-1, c)
        if grid[l][c] == "7":
            return get_next_tile("left", l, c-1)
        if grid[l][c] == "F":
            return get_next_tile("right", l, c+1)

    if from_dir == "right":
        if grid[l][c] == "-":
            return get_next_tile("right", l, c+1)
        if grid[l][c] == "J":
            return get_next_tile("top", l-1, c)
        if grid[l][c] == "7":
            return get_next_tile("bottom", l+1, c)

    if from_dir == "bottom":
        if grid[l][c] == "|":
            return get_next_tile("bottom", l+1, c)
        if grid[l][c] == "L":
            return get_next_tile("right", l, c+1)
        if grid[l][c] == "J":
            return get_next_tile("left", l, c-1)

    if from_dir == "left":
        if grid[l][c] == "-":
            return get_next_tile("left", l, c-1)
        if grid[l][c] == "F":
            return get_next_tile("bottom", l+1, c)
        if grid[l][c] == "L":
            return get_next_tile("top", l-1, c)

    return 'done'


counter = 0

if grid[line-1][col] in top:
    get_next_tile("top", line-1, col)

elif grid[line][col+1] in right:
    get_next_tile("right", line, col+1)

elif grid[line+1][col] in bottom:
    get_next_tile("bottom", line+1, col)

elif grid[line][col-1] in left:
    get_next_tile("left", line, col-1)

pp(f"\n>> final counter: {counter}")
pp(f"\n>> passed_slots: {len(passed_slots.keys())}")

output = ""
for l in range(len(grid)):
    for c in range(len(grid[0])):
        if (l,c) in passed_slots:
            output += "X"
        else:
            if grid[l][c] == ".":
                output += "."
            else:
                output += " "
    output += "\n"

pp(output)

open("days/10/output.txt", "a").write(output)
