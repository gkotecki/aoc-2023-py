import os
import pprint
import re

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/12/input.txt").read().splitlines()
lines = open("days/12/example.txt").read().splitlines()  # 21 arrangements
#       ???.###              1,1,3    - 1  arrangement
#       .??..??...?##.       1,1,3    - 4  arrangements
#       ?#?#?#?#?#?#?#?      1,3,1,6  - 1  arrangement
#       ????.#...#...        4,1,1    - 1  arrangement
#       ????.######..#####.  1,6,5    - 4  arrangements
#       ?###????????         3,2,1    - 10 arrangements

pp(lines)

count = 0

entries = [x.split() for x in lines]
for str_map, str_count in entries:
    c_count = list(map(int, str_count.split(",")))
    print(f"\n>> checking   {str_map}   for: {c_count}")

    split_map = [x for x in str_map.split(".") if x]



print(f"\n>> count: {count}")
