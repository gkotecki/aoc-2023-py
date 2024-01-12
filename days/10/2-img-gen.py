import os
import pprint

from PIL import Image

import sys
sys.setrecursionlimit(100_000)

os.system("clear")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/10/input.txt").read().splitlines()
# lines = open("days/10/example1-2.txt").read().splitlines() # 4 tiles
# lines = open("days/10/example2-2.txt").read().splitlines() # 8 tiles
# lines = open("days/10/example3-2.txt").read().splitlines() # 10 tiles

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

passed_slots = {}

def get_next_tile(from_dir, l, c):
    pp(f"current pos: {(l, c)}: {grid[l][c]}")

    if from_dir == "top":
        if grid[l][c] == "|":
            passed_slots[(l, c)] = (from_dir, "top")
            return get_next_tile("top", l-1, c)
        if grid[l][c] == "7":
            passed_slots[(l, c)] = (from_dir, "left")
            return get_next_tile("left", l, c-1)
        if grid[l][c] == "F":
            passed_slots[(l, c)] = (from_dir, "right")
            return get_next_tile("right", l, c+1)

    if from_dir == "right":
        if grid[l][c] == "-":
            passed_slots[(l, c)] = (from_dir, "right")
            return get_next_tile("right", l, c+1)
        if grid[l][c] == "J":
            passed_slots[(l, c)] = (from_dir, "top")
            return get_next_tile("top", l-1, c)
        if grid[l][c] == "7":
            passed_slots[(l, c)] = (from_dir, "bottom")
            return get_next_tile("bottom", l+1, c)

    if from_dir == "bottom":
        if grid[l][c] == "|":
            passed_slots[(l, c)] = (from_dir, "bottom")
            return get_next_tile("bottom", l+1, c)
        if grid[l][c] == "L":
            passed_slots[(l, c)] = (from_dir, "right")
            return get_next_tile("right", l, c+1)
        if grid[l][c] == "J":
            passed_slots[(l, c)] = (from_dir, "left")
            return get_next_tile("left", l, c-1)

    if from_dir == "left":
        if grid[l][c] == "-":
            passed_slots[(l, c)] = (from_dir, "left")
            return get_next_tile("left", l, c-1)
        if grid[l][c] == "F":
            passed_slots[(l, c)] = (from_dir, "bottom")
            return get_next_tile("bottom", l+1, c)
        if grid[l][c] == "L":
            passed_slots[(l, c)] = (from_dir, "top")
            return get_next_tile("top", l-1, c)

    return 'done'


if grid[line-1][col] in top:
    get_next_tile("top", line-1, col)

elif grid[line][col+1] in right:
    get_next_tile("right", line, col+1)

elif grid[line+1][col] in bottom:
    get_next_tile("bottom", line+1, col)

elif grid[line][col-1] in left:
    get_next_tile("left", line, col-1)

pp(f"\n>> passed_slots: {len(passed_slots.keys())}")

image = Image.new("RGB", (len(grid[0])*3, len(grid)*3))

def triple_pixel(coord, color, accent = None):
    x, y = coord
    for i in range(3):
        for j in range(3):
            image.putpixel((x*3+i,y*3+j), color)
            if accent:
                image.putpixel((x*3+1,y*3+1), accent)

for l in range(len(grid)):
    for c in range(len(grid[0])):
        if (l,c) in passed_slots:
            triple_pixel((c,l), (0,255,0), (0,150,0)) # "X"
            from_dict = {"top": (1,0), "right": (0,-1), "bottom": (-1,0), "left": (0,1)}
            to_dict   = {"top": (-1,0), "right": (0,1), "bottom": (1,0), "left": (0,-1)}
            _from, _to = passed_slots[(l,c)]
            image.putpixel((c*3+1+from_dict[_from][1], l*3+1+from_dict[_from][0]), (0,200,0))
            image.putpixel((c*3+1+to_dict[_to][1], l*3+1+to_dict[_to][0]), (0,200,0))
        else:
            if grid[l][c] == ".":
                triple_pixel((c,l), (0,0,255), (0,0,225)) # "."
            elif grid[l][c] == "S":
                triple_pixel((c,l), (255,50,255), (0,200,0)) # "S"
            else:
                triple_pixel((c,l), (255,0,0), (200,0,0)) # " "

image.save("days/10/output.png")
