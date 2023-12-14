import os
import pprint

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/06/input.txt").read().splitlines()
# lines = open("days/06/example.txt").read().splitlines()

inputs = [x.split()[1:] for x in lines]
time = int("".join(inputs[0]))
record = int("".join(inputs[1]))

winnerCount = 0
for i in range(time):
    distance = (i) * (time - i)
    if distance > record:
        winnerCount += 1

pp(winnerCount)
