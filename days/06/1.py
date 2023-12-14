import os
import pprint

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/06/input.txt").read().splitlines()
lines = open("days/06/example.txt").read().splitlines()

inputs = [list(map(int, x.split()[1:])) for x in lines]
races = [
    (inputs[0][i], inputs[1][i]) for i in range(len(inputs[0]))
]  # [(time, distance), ...]

pp(races)


def getDistance(chargeTime: int, timeWindow: int):
    return chargeTime * timeWindow

winningPossibilities = []

for time, record in races:
    """
    1 >> 1*6 = 6
    2 >> 2*5 = 10
    3 >> 3*4 = 12
    4 >> 4*3 = 12
    5 >> 5*2 = 10
    6 >> 6*1 = 6
    """
    winnerCount = 0
    for i in range(time):
        distance = (i) * (time - i)
        if distance > record:
            winnerCount += 1
    winningPossibilities.append(winnerCount)

pp(winningPossibilities)

product = 1
for item in winningPossibilities:
    product *= item

print(product)
