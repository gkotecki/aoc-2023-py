import os
import pprint
from typing import List

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/11/input.txt").read().splitlines()
# lines = open("days/11/example.txt").read().splitlines()
# 374 with 1
# 1030 with 10
# 8410 with 100

pp(lines)

empty_space = 999_999

galaxies = []

for l, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "#":
            galaxies.append((l, c))

pp(galaxies)

empty_lines = []
empty_cols = []

for l, line in enumerate(lines):
    if "#" not in line:
        empty_lines.append(l)

for col in range(len(lines[0])):
    col_str = ""
    for row in range(len(lines)):
        col_str += lines[row][col]
    if "#" not in col_str:
        empty_cols.append(col)

empty_lines.sort()
empty_cols.sort()

pp(empty_lines)
pp(empty_cols)

sum = 0

a, b = 0, len(galaxies)-1
while a < b:
    while a < b:
        ay,ax, by,bx = galaxies[a][0], galaxies[a][1], galaxies[b][0], galaxies[b][1]

        extra_y = 0
        for line in empty_lines:
            if ay<line<by or by<line<ay:
                extra_y += 1

        extra_x = 0
        for col in empty_cols:
            if ax<col<bx or bx<col<ax:
                extra_x += 1

        dy = abs(ay - by) + extra_y*empty_space
        dx = abs(ax - bx) + extra_x*empty_space
        distance = dy + dx

        # pp(f"Comparing {a},{b}  >>  {(ax,ay)}  {bx,by}  >>  {distance} == {orig_dists.pop(0)}")

        sum += distance
        a += 1
    a = 0
    b -= 1

pp(f"Final sum {sum}")
