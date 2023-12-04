import time

t0 = time.perf_counter()
# Import data
with open("Day 3/input.txt", "r") as infile:
    input = infile.read().splitlines()

# Set size of grid
row_len = len(input[0])
col_len = len(input)

# Create list to hold coordinates of all symbols
symbol_coords_list = []
# Iterate over all coordinates to identify all symbols, and add coordiantes to list in format (y, x) to match order of list index syntax
for y, row in enumerate(input):
    for x, col in enumerate(row):
        if not col.isdigit() and not col == ".":
            symbol_coords_list.append((y, x))


# Function to return all surrounding coordinates of a given coordinate, within the bounds of the total area, and not including the given coordinate
def find_adjacent_coords(y, x, row_len, col_len):
    """Input coordinates of symbol as y, x, returns a tuple of coordiantes of all adjacent coords"""
    adjacent_coords = [
        (y - 1, x - 1),
        (y - 1, x),
        (y - 1, x + 1),
        (y, x - 1),
        (y, x + 1),
        (y + 1, x - 1),
        (y + 1, x),
        (y + 1, x + 1),
    ]

    # Filter out coordinates that are out of bounds
    valid_coords = [
        (i, j) for i, j in adjacent_coords if 0 <= i < col_len and 0 <= j < row_len
    ]

    return valid_coords


# Create list to store all adjacent coordinates, i.e. all coordinates to be tested, generate them, and append to the list
all_adjacent_coords = []
for x, y in symbol_coords_list:
    all_adjacent_coords.extend(find_adjacent_coords(x, y, row_len, col_len))

# List to store all coordinates already counted, to prevent double counting numbers with two or more adjacent symbols
coords_already_counted = []

# List to store all valid numbers to be counted
part_numbers_to_sum = []

# Loop through all coodinates in `all_adjacent_coords`, check if the coordinate is a number, identify the full number (i.e. ..3.. = 3, 123.. = 123, 1.23. = 23, 1.3.5 = 3). Add the full identified number to `part_numbers_to_sum`, and add any coordinates that have been counted to `coords_already_counted`
for y, x in all_adjacent_coords:
    if (y, x) not in coords_already_counted:
        if input[y][x].isdigit():
            coords_already_counted.append((y, x))
            if input[y][x - 1].isdigit():
                coords_already_counted.append((y, x - 1))
                if input[y][x - 2].isdigit():
                    part_numbers_to_sum.append(int(input[y][x - 2 : x + 1]))
                    coords_already_counted.append((y, x - 2))
                else:
                    if input[y][x + 1].isdigit():
                        part_numbers_to_sum.append(int(input[y][x - 1 : x + 2]))
                        coords_already_counted.append((y, x + 1))
                    else:
                        part_numbers_to_sum.append(int(input[y][x - 1 : x + 1]))
            else:
                if input[y][x + 1].isdigit():
                    coords_already_counted.append((y, x + 1))
                    if input[y][x + 2].isdigit():
                        part_numbers_to_sum.append(int(input[y][x : x + 3]))
                        coords_already_counted.append((y, x + 2))
                    else:
                        part_numbers_to_sum.append(int(input[y][x : x + 2]))
                else:
                    part_numbers_to_sum.append(int(input[y][x : x + 1]))


print(f"Part One: {sum(part_numbers_to_sum):>9}")

# Part Two

# Create list to store coordinates of all `*` symbols, identify them, and append to list
gear_coords_list = []

for y, row in enumerate(input):
    for x, col in enumerate(row):
        if col == "*":
            gear_coords_list.append((y, x))

# List to store the sum of all gear ratios identified
gear_total = 0

# Instead of creating one list of all coordinates to loop through as above, this creates a list for each gear, then finds the adjacent numbers for that gear, multiplies them to get the gear ratio, and adds that number to the `gear_total`
all_adjacent_coords_gears = []
for x, y in gear_coords_list:
    gear_adjacent_nums = []
    adjacent_gear_coords = find_adjacent_coords(x, y, row_len, col_len)
    for y, x in adjacent_gear_coords:
        if input[y][x].isdigit():
            if input[y][x - 1].isdigit():
                if input[y][x - 2].isdigit():
                    gear_adjacent_nums.append(int(input[y][x - 2 : x + 1]))
                else:
                    if input[y][x + 1].isdigit():
                        gear_adjacent_nums.append(int(input[y][x - 1 : x + 2]))
                    else:
                        gear_adjacent_nums.append(int(input[y][x - 1 : x + 1]))
            else:
                if input[y][x + 1].isdigit():
                    if input[y][x + 2].isdigit():
                        gear_adjacent_nums.append(int(input[y][x : x + 3]))
                    else:
                        gear_adjacent_nums.append(int(input[y][x : x + 2]))
                else:
                    gear_adjacent_nums.append(int(input[y][x : x + 1]))
    # Here a simple set can be used to remove numbers counted twice.
    gear_num = list(set(gear_adjacent_nums))
    if len(gear_num) == 2:
        gear_total += gear_num[0] * gear_num[1]

print(f"Part Two: {gear_total:>9}")

print(f"Time taken: {time.perf_counter() - t0:.3f} s")
