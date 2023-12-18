import os
import pprint

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/08/input.txt").read().splitlines()
# lines = open("days/08/example.txt").read().splitlines()
# lines = open("days/08/example2.txt").read().splitlines()
# lines = open("days/08/example3.txt").read().splitlines()

instructions = lines[0]

dir_map = {}
for str in lines[2:]:
    key, value = str.split(" = ")
    dir_map[key] = (value[1:4], value[6:9])

pp(instructions)
pp(dir_map)

starting_nodes = list(filter(lambda x: x[2] == "A", dir_map.keys()))
possible_steps = []

def navigate(current_pos, steps):
    for dir in instructions:
        idx = 0 if dir == "L" else 1
        current_pos = dir_map[current_pos][idx]
        steps += 1
        if current_pos[2] == "Z":
            print(steps)
            possible_steps.append(steps)
            break
    else:
        navigate(current_pos, steps)

for node in starting_nodes:
    navigate(node, 0, 0)

pp(sorted(possible_steps))

pp(43*263*53*59*67*73*79)

