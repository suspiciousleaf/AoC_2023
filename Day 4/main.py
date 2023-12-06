import time

t0 = time.perf_counter_ns()
# Import data
with open("Day 4/input.txt", "r") as infile:
    input = [line.split(":")[1].strip() for line in infile.read().splitlines()]

# Create two lists, one with the winning numbers for the card, and one with the numbers for that card
winning_numbers, cards = zip(
    *[
        (set(line.split("|")[0].split()), set(line.split("|")[1].split()))
        for line in input
    ]
)

# Creats a dictionary with card number: {"matches":, "copies":1}. "matches" is the number of winning numbers for the card, "copies" is the number of copies of that card for part 2
cards_dict = {
    (i + 1): {
        "matches": len(winning_numbers[i].intersection(cards[i])),
        "copies": 1,
    }
    for i, _ in enumerate(cards)
}

# Calculates the pounts for each card, and sums them up
total = sum(
    [
        2 ** (len(winning_numbers[i].intersection(cards[i])) - 1)
        for i, _ in enumerate(cards)
        if 2 ** (len(winning_numbers[i].intersection(cards[i])) - 1) >= 1
    ]
)


t1 = time.perf_counter_ns()
print(f"Part One: {total:>9,} time taken: {((t1-t0)/1000000):,.3f} ms")

# Adds copies for cards for each winning pard as per part 2 instructions
for item in cards_dict.items():
    add_cards = list(range(item[0] + 1, item[0] + 1 + item[1]["matches"]))
    for card in add_cards:
        cards_dict[card]["copies"] += item[1]["copies"]

# Calculates the total number of copies of cards for Part 2 answer
total_copies = sum([cards_dict[item]["copies"] for item in cards_dict])

print(
    f"Part Two: {total_copies:>9,} time taken: {((time.perf_counter_ns()-t1)/1000000):,.3f} ms"
)

# Typical run time on my 7 year old laptop, pt1: 2.400 ms, pt2: 0.600 ms
