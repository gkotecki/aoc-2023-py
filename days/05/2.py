import os
import pprint

os.system("clear")
os.system("cls")

printer = pprint.PrettyPrinter(indent=4)


def pp(lines):
    printer.pprint(lines)


file_path = "days/05/input.txt"
# file_path = "days/05/example.txt"

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
        sourceStart, destStart, size = list(map(int, line.split()))
        if value >= sourceStart and value <= (sourceStart + size):
            return destStart + (value - sourceStart)
    return value


# seed_to_soil = lines[3:5]
# soil_to_fertilizer = lines[7:10]
# fertilizer_to_water = lines[12:16]
# water_to_light = lines[18:20]
# light_to_temperature = lines[22:25]
# temperature_to_humidity = lines[27:29]
# humidity_to_location = lines[31:]

seed_to_soil = lines[3:20]
soil_to_fertilizer = lines[22:53]
fertilizer_to_water = lines[55:94]
water_to_light = lines[96:113]
light_to_temperature = lines[115:134]
temperature_to_humidity = lines[136:166]
humidity_to_location = lines[168:]

seedInputs = list(map(int, lines[0].split()[1:]))
seedRanges = [(seedInputs[i], seedInputs[i] + seedInputs[i + 1]) for i in range(0, len(seedInputs), 2)]

smallestLocation = 0

while True:
    if smallestLocation % 50_000 == 0:
        pp(f'location: {smallestLocation/60_294_664 *100:.2f}%')

    humidity = find_in(humidity_to_location, smallestLocation)
    temperature = find_in(temperature_to_humidity, humidity)
    light = find_in(light_to_temperature, temperature)
    water = find_in(water_to_light, light)
    fertilizer = find_in(fertilizer_to_water, water)
    soil = find_in(soil_to_fertilizer, fertilizer)
    seed = find_in(seed_to_soil, soil)

    if any(start <= seed < end for start, end in seedRanges):
        print(f"Seed: {seed}, Location: {smallestLocation}")
        break

    smallestLocation += 1

# pp(smallestLocation)
