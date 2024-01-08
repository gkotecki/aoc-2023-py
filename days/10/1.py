import os
import pprint
from typing import List

os.system("clear")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/10/input.txt").read().splitlines()
lines = open("days/10/example1.txt").read().splitlines()
# lines = open("days/10/example2.txt").read().splitlines()

tile_grid = [list(x) for x in lines]

pp(tile_grid)

top = "|7F"
right = "-J7"
bottom = "|LJ"
left = "-FL"

start = (0,0)
for x in range(len(tile_grid)):
    for y in range(len(tile_grid[0])):
        if tile_grid[x][y] == "S":
            start = (x,y)

pp(start)

