with open("Day 10/input.txt", "r") as infile:
    input = infile.read().splitlines()

input = [list(line) for line in input]

con = {
    "-": ((0, -1), (0, 1)),
    "7": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "|": ((-1, 0), (1, 0)),
    "L": ((-1, 0), (0, 1)),
    "F": ((1, 0), (0, 1)),
}

pos = next(
    (i, j) for i, row in enumerate(input) for j, cell in enumerate(row) if cell == "S"
)
input[pos[0]][pos[1]] = "|"  # For ex1 & ex2: "F"

visited_tiles = [pos]

next_step_available = True

while next_step_available:
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
