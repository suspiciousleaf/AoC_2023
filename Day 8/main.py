import math

with open("Day 8/input.txt", "r") as infile:
    input = [line for line in infile.read().splitlines()]

instructions = [int(num) for num in (input[0].replace("R", "1").replace("L", "0"))]

route = {}
for entry in input[2:]:
    entry_split = entry.split()
    route[entry_split[0]] = [
        entry_split[2].replace("(", "").replace(",", ""),
        entry_split[3].replace(")", ""),
    ]

pos = "AAA"
steps = 0

finished = False

while finished == False:
    for step in instructions:
        steps += 1
        pos = route[pos][step]
        if pos == "ZZZ":
            finished = True

print(f"Part One: {steps}")

# Part Two

pos_list = [item for item in route if item[-1:] == "A"]

min_paths = []
for x in pos_list:
    steps_two = 0
    finished_two = False
    while finished_two == False:
        for step in instructions:
            steps_two += 1
            x = route[x][step]
            if x[-1] == "Z":
                finished_two = True
    min_paths.append(steps_two)

print(f"Part Two: {math.lcm(*min_paths):,}")
