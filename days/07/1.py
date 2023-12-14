import os
import pprint

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/07/input.txt").read().splitlines()
# lines = open("days/07/example.txt").read().splitlines()

entries = [x.split() for x in lines]  # [ [hand, bid], ...]

"""
Types:
5, 4, 3+2, 3, 2+2, 2, highest
on type draw, sequential highest from first
"""

sequence = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
types = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]

pp(lines)
pp(entries)

ranking = {}

for i, (cards, bid) in enumerate(entries):
    handDict = {}
    for card in cards:
        if card in handDict:
            handDict[card] += 1
        else:
            handDict[card] = 1
    typeScore = sorted(handDict.values(), reverse=True)
    cardScore = [sequence.index(x) for x in cards]
    ranking[i] = {
        "cards": cards,
        "bid": bid,
        "type": types.index(typeScore),
        "score": cardScore
    }

ranked = sorted(ranking.values(), key=lambda x: (x["type"], x["score"]), reverse=True)

# products = []
sumProducts = 0
for i in range(len(ranked)):
    product = int(ranked[i]["bid"]) * (i + 1)
    # products.append(product)
    sumProducts += product

pp(ranked)
# pp(products)
pp(sumProducts)
