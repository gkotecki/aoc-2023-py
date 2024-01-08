import os
import pprint
from typing import List

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/09/input.txt").read().splitlines()
# lines = open("days/09/example.txt").read().splitlines()

histories = [list(map(int, x.split())) for x in lines]

pp(histories)


def extrapolate(items: list[int]) -> int:
    pp(f"extrapolate({items})")
    diffs = []
    all_zeroes = True
    for i in range(len(items) - 1):
        diff = items[i + 1] - items[i]
        diffs.append(diff)
        if diff != 0:
            all_zeroes = False
    if all_zeroes:
        return items[0]
    return items[0] - extrapolate(diffs)

sum = 0
for history in histories:
    next = extrapolate(history)
    print(next)
    sum += next

pp(sum)
