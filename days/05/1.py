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

lines = [
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",  # 79>81  14>14  55>57  13>13
    "50 98 2",  # destination range start of 50, a source range start of 98, and a range length of 2
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]
# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35
# So, the lowest location number in this example is 35

pp(lines)

def buildDict(lines):
    result = {}
    for line in lines:
        destStart, sourceStart, length = line.split()
        for i in range(int(length)):
            result[int(sourceStart) + i] = int(destStart) + i
    return result

soilMap = buildDict(lines[3:5])
fertilizerMap = buildDict(lines[7:10])
waterMap = buildDict(lines[12:16])
lightMap = buildDict(lines[18:20])
temperatureMap = buildDict(lines[22:25])
humidityMap = buildDict(lines[27:29])
locationMap = buildDict(lines[31:33])

# soilMap = buildDict(lines[4:21])
# fertilizerMap = buildDict(lines[23:54])
# waterMap = buildDict(lines[56:95])
# lightMap = buildDict(lines[97:114])
# temperatureMap = buildDict(lines[116:135])
# humidityMap = buildDict(lines[137:167])
# locationMap = buildDict(lines[169:])

seeds = list(map(int, lines[0].split()[1:]))
locations = []

for seed in seeds:
    soil = soilMap.get(seed, seed)
    fertilizer = fertilizerMap.get(soil, soil)
    water = waterMap.get(fertilizer, fertilizer)
    light = lightMap.get(water, water)
    temperature = temperatureMap.get(light, light)
    humidity = humidityMap.get(temperature, temperature)
    location = locationMap.get(humidity, humidity)
    locations.append(location)

pp(min(locations))
