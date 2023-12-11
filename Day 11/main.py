from itertools import combinations

with open("Day 11/input.txt", "r") as infile:
    input = infile.read().splitlines()

# Find indices of all rows and columns that have no galaxy, "#", so they can be expanded the required number of times
vertical_indices = [i for i, line in enumerate(input) if "#" not in line]

horizontal_indices = [
    x for x in range(len(input[0])) if "#" not in [row[x] for row in input]
]

# Find coordinates of all galaxies
gal_coords = [
    (y, x) for y, row in enumerate(input) for x, cell in enumerate(row) if cell == "#"
]
# Find all pair combinations of galaxies
all_combinations = list(combinations(gal_coords, 2))


# Returns range objects for Manhattan path between coordinates. One for vertical path, one for horizontal.
def manhattan_range(coord):
    y1, x1 = coord[0]
    y2, x2 = coord[1]
    y = range(min(y1, y2), max(y1, y2))
    x = range(min(x1, x2), max(x1, x2))
    return (y, x)


# For each path between galaxy pairs, calculates the Manhattan distance between them, and the number of intersections with the lines to be expanded. Adds the expansion factor for each intersection, 1 for part 1 (line is doubled), and 999,999 for part 2 (line multiplied by 1,000,000). Add each total distance for that path to a list so they can be summed for the final answer.
distances_1, distances_2 = [], []
for path in all_combinations:
    distance_1 = sum([len(x) for x in manhattan_range(path)])
    distance_2 = sum([len(x) for x in manhattan_range(path)])
    y_path, x_path = manhattan_range(path)
    for index in vertical_indices:
        if index in y_path:
            distance_1 += 1
            distance_2 += -1 + 1000000
    for index in horizontal_indices:
        if index in x_path:
            distance_1 += 1
            distance_2 += -1 + 1000000
    distances_1.append(distance_1)
    distances_2.append(distance_2)

print(f"Part One: {sum(distances_1):,}")
print(f"Part Two: {sum(distances_2):,}")
