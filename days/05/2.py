import os
import pprint

os.system("clear")
os.system("cls")

printer = pprint.PrettyPrinter(indent=4)


def pp(lines):
    printer.pprint(lines)


file_path = "days/05/input.txt"
file_path = "days/05/example.txt"

with open(file_path, "r") as file:
    contents = file.read()

# sections = contents.split("\n\n")

# pp(sections)

# inputs = [int(x) for x in sections[0].split()[1:]]
# # [(start,end), ...]
# seeds = [(inputs[i], inputs[i] + inputs[i + 1]) for i in range(0, len(inputs), 2)]
# # [[d_start, s_start, size], ...]
# mapInputs = [[list(map(int, x.split())) for x in y.splitlines()[1:]] for y in sections[1:]]


# pp(seeds)
# pp(mapInputs)

# https://github.com/xHyroM/aoc/blob/main/2023/05/second_without_bruteforce.py
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/5.py
# https://github.com/mgtezak/Advent_of_Code/blob/master/2023/Day_05.py

















lines = contents.split("\n")
pp(lines)


def find_in(lines: list[str], value: int):
    for line in lines:
        destStart, sourceStart, length = list(map(int, line.split()))
        if value >= sourceStart and value <= (sourceStart + length):
            return destStart + (value - sourceStart)
    return value


seed_to_soil = lines[3:5]
soil_to_fertilizer = lines[7:10]
fertilizer_to_water = lines[12:16]
water_to_light = lines[18:20]
light_to_temperature = lines[22:25]
temperature_to_humidity = lines[27:29]
humidity_to_location = lines[31:]

# seed_to_soil = lines[3:20]
# soil_to_fertilizer = lines[22:53]
# fertilizer_to_water = lines[55:94]
# water_to_light = lines[96:113]
# light_to_temperature = lines[115:134]
# temperature_to_humidity = lines[136:166]
# humidity_to_location = lines[168:]

seedInputs = list(map(int, lines[0].split()[1:]))
seedPairs = [(seedInputs[i], seedInputs[i + 1]) for i in range(0, len(seedInputs), 2)]
smallestLocation = float('inf')

for start, size in seedPairs:
    pp(f'>> checking pair {start}, {size}')
    for i in range(size):
        if i % 2 == 0:
            pp(f'{i/size * 100:.2f} %')
        seed = start + i
        soil = find_in(seed_to_soil, seed)
        fertilizer = find_in(soil_to_fertilizer, soil)
        water = find_in(fertilizer_to_water, fertilizer)
        light = find_in(water_to_light, water)
        temperature = find_in(light_to_temperature, light)
        humidity = find_in(temperature_to_humidity, temperature)
        location = find_in(humidity_to_location, humidity)
        smallestLocation = min(location, smallestLocation)

pp(smallestLocation)
