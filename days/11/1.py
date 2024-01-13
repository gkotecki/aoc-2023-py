import os
import pprint
from typing import List

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/11/input.txt").read().splitlines()
lines = open("days/11/example.txt").read().splitlines()
# 1030 with 10
# 8410 with 100

# pp(lines)

empty_space = 99
expanded_universe = []

for line in lines:
    expanded_universe.append(line)
    if "#" not in line:
        for i in range(empty_space):
            expanded_universe.append(line)

empty_space_col_idxs = []
for col in range(len(lines[0])):
    col_str = ""
    for row in range(len(lines)):
        col_str += lines[row][col]
    if "#" not in col_str:
        for i in range(empty_space):
            empty_space_col_idxs.append(col)

while empty_space_col_idxs:
    idx = empty_space_col_idxs.pop()
    for row in range(len(expanded_universe)):
        expanded_universe[row] = expanded_universe[row][:idx] + "." + expanded_universe[row][idx:]

# pp(expanded_universe)

galaxies = []

for l, line in enumerate(expanded_universe):
    for c, char in enumerate(line):
        if char == "#":
            galaxies.append((l, c))

# pp(galaxies)

sum = 0

a, b = 0, len(galaxies)-1
while a < b:
    while a < b:
        distance = abs(galaxies[a][0] - galaxies[b][0]) + abs(galaxies[a][1] - galaxies[b][1])
        # pp(f"Comparing {a},{b} >> {galaxies[a]} {galaxies[b]} >> {distance}")
        sum += distance
        a += 1
    a = 0
    b -= 1

pp(f"Final sum {sum}")
