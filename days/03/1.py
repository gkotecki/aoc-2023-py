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
#     "467..114..",  # 114 not adjacent to any symbol
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",  # 58 not adjacent to any symbol
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598..",
# ]

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

    xStart = max(x - 1, 0)
    xEnd = min(x + len(num), len(line) - 1)

    upperBorder = lines[y - 1][xStart : xEnd + 1] if y > 0 else ""
    sideChars = line[xStart] + line[xEnd]
    lowerBorder = lines[y + 1][xStart : xEnd + 1] if y < len(lines) - 1 else ""

    borders = upperBorder + sideChars + lowerBorder

    adjacent = False
    for c in borders:
        if c not in (nums + "."):
            adjacent = True
            break

    return {"number": int(num), "adjacent": adjacent, "length": len(num)}


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

filteredSum = 0
for num in foundNumbers:
    if num["adjacent"]:
        filteredSum += num["number"]

pp(filteredSum)
