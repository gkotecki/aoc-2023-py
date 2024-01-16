from functools import cache
import os
import pprint
import re

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/14/input.txt").read().splitlines()
# lines = open("days/14/example.txt").read().splitlines()

# @cache
def roll_north(lines: list[str]) -> list[str]:
    char_list = [list(line) for line in lines]  # Convert strings to lists

    for l, line in enumerate(char_list):
        for c, char in enumerate(line):
            acc = 1
            while char == "." and l+acc < len(lines) and lines[l+acc][c] is not "#":
                if lines[l+acc][c] == "O":
                    char_list[l+acc-1][c] = "O"
                    char_list[l+acc][c] = "."
                acc += 1

    lines = ["".join(line) for line in char_list]  # Convert lists back to strings
    return lines

def calculate_weight(lines: list[str]) -> int:
    total = 0
    for i in range(len(lines)):
        weight = len(re.findall(r"O", lines[len(lines)-1 - i])) * (1 + i)
        total += weight
    return total

# pp(lines)
rolled_lines = roll_north(lines)
for i in range(50):
    rolled_lines = roll_north(rolled_lines)

pp(rolled_lines)
total_weight = calculate_weight(rolled_lines)
print(f"\n>> total_weight: {total_weight}")
