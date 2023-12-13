import os
import pprint

os.system("clear")
os.system("cls")

printer = pprint.PrettyPrinter(indent=4)


def pp(lines):
    printer.pprint(lines)


file_path = "days/04/input.txt"

with open(file_path, "r") as file:
    contents = file.read()

lines = contents.split("\n")

# lines = [
#     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",  # 4 matches, copy 2,3,4,5
#     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",  # 2 matches, copy 3,4
#     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",  # 2 matches, copy 4,5
#     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",  # 1 matches, copy 5
#     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",  # none
#     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",  # none
# ]  # sums:  1(1) + 2(2) + 4(3) + 8(4) + 14(5) + 1(6) = 36(total)

pp(lines)

matchDict = {}

for entry in lines:
    card, data = entry.split(": ")
    cardKey = int(card.split()[1])
    winners, available = data.split(" | ")

    winners = list(map(int, winners.split()))
    available = list(map(int, available.split()))

    matches = list(filter(lambda x: x in winners, available))

    matchDict[cardKey] = len(matches)

pp(matchDict)

cardCount = 0


def appendToCount(card):
    global cardCount
    cardCount += 1
    newCards = matchDict[card]
    if newCards == 0:
        return
    for i in range(newCards):
        appendToCount(card + i + 1)


for card in matchDict.keys():
    appendToCount(card)

pp(cardCount)
