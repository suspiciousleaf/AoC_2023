with open("Day 6/input.txt", "r") as infile:
    input = [
        line.strip()
        for line in infile.read()
        .replace("Time:", "")
        .replace("Distance:", "")
        .splitlines()
    ]

# Creates a list of all times and distances
times = [int(num) for num in input[0].split()]
distances = [int(num) for num in input[1].split()]


def calculate_options(times, distances):
    # Calculates options of time and distance, checks which will win, and multiplies them together
    total_options = 1
    for i, race in enumerate(times):
        possible_wins = 0
        options = range(1, race)
        for option in options:
            distance = option * (race - option)
            if distance > distances[i]:
                possible_wins += 1
        total_options *= possible_wins
    return total_options


print(f"Part One: {calculate_options(times, distances)}")

# Finds the single value for time and distance as per Part Two, and creates a list of one value so it can be used by the function from part one
times_two = [int("".join([num for num in input[0] if num.isdigit()]))]
distances_two = [int("".join([num for num in input[1] if num.isdigit()]))]

print(f"Part Two: {calculate_options(times_two, distances_two)}")
