# Import data
with open("Day 1\input.txt", "r") as infile:
    input = infile.readlines()


def find_values(input):
    # Creates nested lists with only the digits (as strings) from each string of mixed digits and letters, eg .
    # ["1two3four", "5six7"] -> [["1", "3"], ["5", "7"]]
    input_digits = [[digit for digit in line if digit.isnumeric()] for line in input]
    # Concatenates the first and last digit for each nested list above, converts to integers, and returns the total, eg.
    # [["1", "3"], ["5", "7"]] -> [13, 57] -> 70
    return sum([int(x[0] + x[-1]) for x in input_digits])


print(f"Part One: {find_values(input)}")


def replace_words(i, char, test_string):
    # Checks if the substring begins with a number as a word, and returns that digit as a string
    if char == "o":
        if test_string[i : i + 3] == "one":
            return "1"
    elif char == "t":
        if test_string[i : i + 3] == "two":
            return "2"
        elif test_string[i : i + 5] == "three":
            return "3"
    elif char == "f":
        if test_string[i : i + 4] == "four":
            return "4"
        elif test_string[i : i + 4] == "five":
            return "5"
    elif char == "s":
        if test_string[i : i + 3] == "six":
            return "6"
        elif test_string[i : i + 5] == "seven":
            return "7"
    elif char == "e":
        if test_string[i : i + 5] == "eight":
            return "8"
    elif char == "n":
        if test_string[i : i + 4] == "nine":
            return "9"


def make_new_string(test_string):
    # Creates a new string with all valid letter combinations replaced with digits, all digits copied over, and returns that string. eg,
    # "1two3foursevenine" -> "123479"
    new_list = []
    for i, char in enumerate(test_string):
        if char.isdigit():
            new_list.append(char)
        else:
            test = replace_words(i, char, test_string)
            if test:
                new_list.append(test)
    return "".join(new_list)


# Creates a new list with all valid words replaced with their digits, which can then be processed like part 1
words_replaced_list = [make_new_string(test_string) for test_string in input]


print(f"Part Two: {find_values(words_replaced_list)}")

list_comp_pt_1 = sum(
    [
        int(x[0] + x[-1])
        for x in [[num for num in line if num.isdigit()] for line in input]
    ]
)

print(f"Part One: {list_comp_pt_1} list comprehension")

# The list comprehension below solves the problem in a somewhat unreadable and unpleasant way, but much less code.
list_comp_pt_2 = sum(
    [
        int(x[0] + x[-1])
        for x in [
            [
                num
                for num in line.replace("one", "o1e")
                .replace("two", "t2")
                .replace("three", "t3e")
                .replace("four", "f4")
                .replace("five", "f5e")
                .replace("six", "s6")
                .replace("seven", "s7n")
                .replace("eight", "e8t")
                .replace("nine", "n9e")
                if num.isdigit()
            ]
            for line in input
        ]
    ]
)

print(f"Part Two: {list_comp_pt_2} list comprehension")
