with open("Day 10/input.txt", "r") as infile:
    input = infile.read().splitlines()

input = [list(line) for line in input]

# Dictionary to give relative coordinates of connected tiles to each symbol
con = {
    "-": ((0, -1), (0, 1)),
    "7": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "|": ((-1, 0), (1, 0)),
    "L": ((-1, 0), (0, 1)),
    "F": ((1, 0), (0, 1)),
}

# Finds the coordinates of the starting tile
pos = next(
    (i, j) for i, row in enumerate(input) for j, cell in enumerate(row) if cell == "S"
)

# Sets starting tile "S" to the correct symbol, done manually as I was too lazy to write the code to do it automatically
input[pos[0]][pos[1]] = "|"  # For ex1 & ex2: "F"

# Create a list to hold coordinates of all tiles in pipe loop, and add starting position
visited_tiles = [pos]

next_step_available = True

# Keep looping until no next step is found, i.e. loop has completed
while next_step_available:
    # Find the next tile based on the current symbol and coordinates. Each tile will return two coordinates, one of which has been visited before, so only the unvisited coordinate is needed
    adj_tiles = [
        tile
        for tile in (
            (
                pos[0] + con[input[pos[0]][pos[1]]][k][0],
                pos[1] + con[input[pos[0]][pos[1]]][k][1],
            )
            for k in range(2)
        )
        if tile not in visited_tiles
    ]
    next_step_available = len(adj_tiles)
    if next_step_available:
        pos = adj_tiles[0]
        visited_tiles.append(pos)

print(f"Part One: {len(visited_tiles) // 2}")

non_pipe_tiles = []

# Replace all tiles that are not part of the loop with ".", and create a list of coordinates of all non loop tiles
for y, row in enumerate(input):
    for x, cell in enumerate(row):
        if (y, x) not in visited_tiles:
            input[y][x] = "."
            non_pipe_tiles.append((y, x))

# Variable to store the total number of inside / enclosed tiles
inside_tiles = 0

# Count the number of times a pipe boundary is crossed, starting from the left. Each boundary will alternate between inside / outside / inside
for y, x in non_pipe_tiles:
    test_line = "".join(input[y][:x])
    pipe_count = test_line.count("|") + test_line.count("F") + test_line.count("7")
    if pipe_count % 2:
        inside_tiles += 1

print(f"Part Two: {inside_tiles}")

# with open("Day 10/output.txt", "w") as outfile:
#     for line in input:
#         outfile.write("".join(line))
#         outfile.write("\n")
