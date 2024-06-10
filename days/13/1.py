import os
import pprint

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


lines = open("days/13/input.txt").read().split("\n\n")
lines = open("days/13/example.txt").read().split("\n\n")

patterns = [x.splitlines() for x in lines]

for lines in patterns:
    print(f"\n>> checking pattern: {lines}")

    h_mirror_ix = None
    for l, line in enumerate(lines):
        if l < len(lines)-1 and line == lines[l+1]:
            print(f">> found equal lines: {line}")
            a,b = l,l+1
            while a >= 0 and b < len(lines):
                a -= 1
                b += 1
                break
            else:
                h_mirror_ix = l
    print(f"h_mirror_ix: {h_mirror_ix}")

    v_mirror_ix = None
    for c, _ in enumerate(lines[0]):
        col = "".join([lines[l][c] for l, _ in enumerate(lines)])
        if c < len(lines[0])-1 and col == "".join([lines[l][c+1] for l, _ in enumerate(lines)]):
            print(f">> found equal cols: {col}")
            a,b = c,c+1
            while a >= 0 and b < len(lines[0]):
                a -= 1
                b += 1
                break
            else:
                v_mirror_ix = c

    print(f"h_mirror_ix: {h_mirror_ix}")
