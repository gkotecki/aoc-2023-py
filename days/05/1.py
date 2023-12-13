import os
import pprint

os.system("clear")
os.system("cls")

printer = pprint.PrettyPrinter(indent=4)


def pp(lines):
    printer.pprint(lines)


file_path = "days/05/input.txt"

with open(file_path, "r") as file:
    contents = file.read()

lines = contents.split("\n")

# lines = [
#     "seeds: 79 14 55 13",
#     "",
#     "seed-to-soil map:",  # 79>81  14>14  55>57  13>13
#     "50 98 2",  # destination range start of 50, a source range start of 98, and a range length of 2
#     "52 50 48",
#     "",
#     "soil-to-fertilizer map:",
#     "0 15 37",
#     "37 52 2",
#     "39 0 15",
#     "",
#     "fertilizer-to-water map:",
#     "49 53 8",
#     "0 11 42",
#     "42 0 7",
#     "57 7 4",
#     "",
#     "water-to-light map:",
#     "88 18 7",
#     "18 25 70",
#     "",
#     "light-to-temperature map:",
#     "45 77 23",
#     "81 45 19",
#     "68 64 13",
#     "",
#     "temperature-to-humidity map:",
#     "0 69 1",
#     "1 0 69",
#     "",
#     "humidity-to-location map:",
#     "60 56 37",
#     "56 93 4",
# ]
# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35
# So, the lowest location number in this example is 35

pp(lines)


def find_in(lines: list[str], value: int):
    for line in lines:
        destStart, sourceStart, length = list(map(int, line.split()))
        if value >= sourceStart and value <= (sourceStart + length):
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

seeds = list(map(int, lines[0].split()[1:]))
locations = []

for seed in seeds:
    soil = find_in(seed_to_soil, seed)
    fertilizer = find_in(soil_to_fertilizer, soil)
    water = find_in(fertilizer_to_water, fertilizer)
    light = find_in(water_to_light, water)
    temperature = find_in(light_to_temperature, light)
    humidity = find_in(temperature_to_humidity, temperature)
    location = find_in(humidity_to_location, humidity)
    locations.append(location)

pp(min(locations))
