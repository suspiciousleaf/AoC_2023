from models import Card

with open("Day 7/input.txt", "r") as infile:
    input = [line.split() for line in infile.read().splitlines()]

cards = [Card(card_info) for card_info in input]

cards_sorted = sorted(cards, key=lambda card: (card.score, card.cards_subbed))

i = len(cards_sorted)

for card in cards_sorted:
    card.rank = i
    card.bid = card.bet * i
    i -= 1

total_winnings = sum([card.bid for card in cards_sorted])
print(f"Part One: {total_winnings}")

# Part Two

cards_pt_2 = sorted(cards, key=lambda card: (card.score_two, card.cards_subbed_no_j))

i = len(cards_pt_2)

for card in cards_pt_2:
    card.rank_two = i
    card.bid_two = card.bet * card.rank_two
    i -= 1


total_winnings_two = sum([card.bid_two for card in cards])
print(f"Part Two: {total_winnings_two}")
