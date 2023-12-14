import os
import pprint

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/08/input.txt").read().splitlines()
# lines = open("days/08/example.txt").read().splitlines()
# lines = open("days/08/example2.txt").read().splitlines()

instructions = lines[0]

dir_map = {}
for str in lines[2:]:
    key, value = str.split(" = ")
    dir_map[key] = (value[1:4], value[6:9])

pp(instructions)
pp(dir_map)

def navigate(current_pos, steps):
    for dir in instructions:
        idx = 0 if dir == "L" else 1
        current_pos = dir_map[current_pos][idx]
        steps += 1
        if current_pos == "ZZZ":
            print(steps)
            break
    else:
        navigate(current_pos, steps)

navigate("AAA", 0)
