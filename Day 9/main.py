with open("Day 9/input.txt", "r") as infile:
    input = infile.read().splitlines()

input = {i: {0: [int(num) for num in line.split(" ")]} for i, line in enumerate(input)}


# function to return a list, with each number being the difference between two numbers in the list given as argument. Pattern is the main dictionary element containing all the derivative difference lists.
def create_diff_list(pattern, input):
    return [
        (input[pattern][i - 1][j + 1] - input[pattern][i - 1][j])
        for j in range(len(input[pattern][i - 1]) - 1)
    ]


# Create lists to hold the new generated numbers
generated_next = []
generated_prev = []

# Loop through inputs to calculate each one
for pattern in input:
    # Create flag to stop loop when the calculated differences are all 0
    finished = False
    i = 1
    while finished == False:
        input[pattern][i] = create_diff_list(pattern, input)
        # Check if the difference list is all 0, and set flag to True to break loop. Otherwise iterate counter to create next level of derivative list
        if all(element == 0 for element in input[pattern][i]):
            finished = True
        else:
            i += 1
    # Loop backwards down through the lists, starting two below the top, and stopping at the bottom
    for neg_step in range(len(input[pattern]) - 2, -1, -1):
        if neg_step >= 0:
            # Next num = last value in list, plus the last value in the difference list above it
            next_num = input[pattern][neg_step][-1] + input[pattern][neg_step + 1][-1]
            # Prev num = first value in list, minus the first value in the difference list above it
            prev_num = input[pattern][neg_step][0] - input[pattern][neg_step + 1][0]
            # Add the generated numbers to the beginning and end of the input sequences (prev_num to index 0, next_num to index -1)
            input[pattern][neg_step].append(next_num)
            input[pattern][neg_step].insert(0, prev_num)
    # Add generated numbers to separate lists so they can be summed to calculate answer
    generated_next.append(input[pattern][0][-1])
    generated_prev.append(input[pattern][0][0])

print(f"Part One: {sum(generated_next)}")
print(f"Part Two: {sum(generated_prev)}")
