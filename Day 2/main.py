# Import data
with open("Day 2\example.txt", "r") as infile:
    input = infile.read().splitlines()

# Set variables for Part 1 & 2 answers
power_sum = 0
game_number_total = 0

# Loop through each game, setting game number, and game details. sum(list, []) is used to flatten the 2d list eg,
# "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue" ->
# game_number = 2
# game_details = [' 1 blue', ' 2 green', ' 3 green', ' 4 blue', ' 1 red', ' 1 green', ' 1 blue']
for game in input:
    game_number = int("".join([num for num in game.split(":")[0] if num.isdigit()]))
    game_details = sum(
        [game_temp.split(",") for game_temp in game.split(":")[1].split(";")], []
    )

    # Set a variable for the max value for red, green, blue achieved across each game
    red_max, green_max, blue_max = 0, 0, 0

    # Loop through each game and identify the max value for each colour
    for item in game_details:
        red = 0
        green = 0
        blue = 0
        if "red" in item:
            red = int("".join([num for num in item if num.isdigit()]))
        elif "green" in item:
            green = int("".join([num for num in item if num.isdigit()]))
        elif "blue" in item:
            blue = int("".join([num for num in item if num.isdigit()]))

        # Set the max value for each colour per game across all sets
        if red > red_max:
            red_max = red
        if green > green_max:
            green_max = green
        if blue > blue_max:
            blue_max = blue

    # Calculate the two values required for the answers
    game_power = red_max * green_max * blue_max
    power_sum += game_power

    if red_max <= 12 and green_max <= 13 and blue_max <= 14:
        game_number_total += game_number

print(f"Part One: {game_number_total}")
print(f"Part Two: {power_sum}")
