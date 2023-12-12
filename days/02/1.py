import os

os.system("clear")
os.system("cls")

file_path = "days/02/input.txt"

with open(file_path, "r") as file:
    contents = file.read()

lines = contents.split("\n")

# lines = [
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
# ]

allowedRed = 12
allowedGreen = 13
allowedBlue = 14

games = {}
for line in lines:
    keyvalue = line.split(":")
    key = keyvalue[0][5:]
    reveals = list(map(lambda x: x.strip().split(", "), keyvalue[1].split(";")))

    games[key] = []
    for colors in reveals:
        dict = {}
        for color in colors:
            if "red" in color:
                dict["red"] = color.split(" ")[0]
            elif "green" in color:
                dict["green"] = color.split(" ")[0]
            elif "blue" in color:
                dict["blue"] = color.split(" ")[0]
        games[key].append(dict)

print(games)

allowedGameIds = set()
for key, reveals in games.items():
    isAllowed = True
    for reveal in reveals:
        if (
            ("red" in reveal and int(reveal["red"]) > allowedRed) or
            ("green" in reveal and int(reveal["green"]) > allowedGreen) or
            ("blue" in reveal and int(reveal["blue"]) > allowedBlue)
        ):
            isAllowed = False
    if isAllowed:
        allowedGameIds.add(key)

print(allowedGameIds)

gameIdsSum = 0
for gameId in allowedGameIds:
    gameIdsSum += int(gameId)
print(gameIdsSum)
