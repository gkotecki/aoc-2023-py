import os
import pprint

os.system("clear")
os.system("cls")

printer = pprint.PrettyPrinter(indent=4)


def pp(lines):
    printer.pprint(lines)


file_path = "days/03/input.txt"

with open(file_path, "r") as file:
    contents = file.read()

lines = contents.split("\n")

# lines = [
#     "467..114..",
#     "...*......",  # gear close to 467 and 35, ratio is 467*35 = 16345
#     "..35..633.",
#     "......#...",
#     "617*......",  # gear not close to exactly 2, not considered
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",  # gear close to 755 and 598, ratio is 755*598 = 451490
#     ".664.598..",
# ]  # all gears add up to 467835

pp(lines)

nums = "0123456789"


def parseNumber(x, y):
    if lines[y][x] not in nums:
        return {"number": None, "adjacent": False, "length": 0}

    line = lines[y]
    num = ""
    for c in line[x:]:
        if c in nums:
            num += c
        else:
            break

    xStart, xEnd = max(x - 1, 0), min(x + len(num), len(line) - 1)
    yStart, yEnd = max(y - 1, 0), min(y + 1, len(lines) - 1)

    adjacentGears = []
    y = yStart
    while y <= yEnd:
        x = xStart
        while x <= xEnd:
            if lines[y][x] == "*":
                adjacentGears.append((x, y))
            x += 1
        y += 1

    return {"number": int(num), "adjacentGears": adjacentGears, "length": len(num)}


foundNumbers = []

for y in range(len(lines)):
    x = 0
    while x < len(lines[y]):
        res = parseNumber(x, y)
        if res["number"]:
            foundNumbers.append(res)
            x += res["length"]
        else:
            x += 1

pp(foundNumbers)

gears = {}

for number in foundNumbers:
    for coord in number["adjacentGears"]:
        if coord in gears:
            gears[coord].append(number["number"])
        else:
            gears[coord] = [number["number"]]

pp(gears)

ratio = 0
for coord in gears:
    if len(gears[coord]) == 2:
        ratio += gears[coord][0] * gears[coord][1]
pp(ratio)
