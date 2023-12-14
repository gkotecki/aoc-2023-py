import os
import pprint

os.system("clear")
os.system("cls")

def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)

lines = open("days/07/input.txt").read().splitlines()
# lines = open("days/07/example.txt").read().splitlines()

entries = [x.split() for x in lines]  # [ [hand, bid], ...]

sequence = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
types = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]

ranking = {}
for i, (cards, bid) in enumerate(entries):
    handDict = {}
    jokers = 0
    for card in cards:
        if card == "J":
            jokers += 1
            continue
        if card in handDict:
            handDict[card] += 1
        else:
            handDict[card] = 1
    typeScore = sorted(handDict.values(), reverse=True)
    cardScore = [sequence.index(x) for x in cards]

    if jokers > 0:
        if jokers == 5:
            typeScore = [5]
        else:
            typeScore[0] += jokers

    ranking[i] = {
        "cards": cards,
        "bid": bid,
        "type": types.index(typeScore),
        "score": cardScore,
    }

ranked = sorted(ranking.values(), key=lambda x: (x["type"], x["score"]), reverse=True)

sumProducts = 0
for i in range(len(ranked)):
    sumProducts += int(ranked[i]["bid"]) * (i + 1)

pp(ranked)
pp(sumProducts)
