import os
import pprint

os.system("clear")
os.system("cls")


def pp(lines):
    pprint.PrettyPrinter(indent=4).pprint(lines)


# sections = open("days/05/example.txt").read().strip().split("\n\n")
sections = open("days/05/input.txt").read().strip().split("\n\n")

inputs = [int(x) for x in sections[0].split()[1:]]

# Seeds format: [(start, end), ...]
seeds = [(inputs[i], inputs[i] + inputs[i + 1]) for i in range(0, len(inputs), 2)]

# Map format: [[destination_range_start, source_range_start, size], ...]
maps = [[list(map(int, x.split())) for x in y.splitlines()[1:]] for y in sections[1:]]

# pp(seeds)
# pp(maps)


def remap(start: int, end: int, new_seeds: list[tuple[int]], m: list[int]) -> int:
    for destination_range_start, source_range_start, size in m:
        # Check if the ranges overlap
        overlap_start = max(start, source_range_start)
        overlap_end = min(end, source_range_start + size)

        if overlap_start < overlap_end:
            new_seeds.append(
                (
                    destination_range_start + (overlap_start - source_range_start),
                    destination_range_start + (overlap_end - source_range_start),
                )
            )

            if start < overlap_start:
                seeds.append((start, overlap_start))

            if overlap_end < end:
                seeds.append((overlap_end, end))

            break
    else:
        # If no overlap, just add the original range to the new seeds
        new_seeds.append((start, end))


for m in maps:
    # pp(f">> m {m}")
    # pp(f">> seeds {seeds}")
    new_seeds = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        remap(start, end, new_seeds, m)
        # pp(new_seeds)

    seeds = new_seeds

print(min(seeds)[0])
