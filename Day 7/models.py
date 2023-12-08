# Dict to substitute cards in a new list so the Card objects can be sorted easily. A K Q J T will not sort correctly, A B C D E will do.
substitute_dict = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "J": "D",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M",
}


class Card:
    # Calculates the hand and assigns a numerical score, 1 = Five of a kind, 2 = Full house, etc
    def get_score_one(self, cards_to_score):
        cards_set = set(cards_to_score)
        different_cards = len(cards_set)

        if different_cards == 1:
            score = 1
        elif different_cards == 4:
            score = 6
        elif different_cards == 5:
            score = 7
        else:
            card_num_dict = {char: self.cards.count(char) for char in cards_set}
            if different_cards == 2:
                if max(card_num_dict.values()) == 4:
                    score = 2
                else:
                    score = 3
            else:
                if max(card_num_dict.values()) == 3:
                    score = 4
                else:
                    score = 5
        return score

    # Calculates the best possible combination for the hand with Jokers acting as wild cards. Jokers are removed before the function is called
    def get_score_two(self, cards_to_score):
        cards_set = set(cards_to_score)
        card_num_list = sorted(
            [self.cards.count(char) for char in cards_set], reverse=True
        )

        # If the list is empty it must have been all Joker cards, so it will have the best possible score
        if not cards_to_score:
            return 1

        if card_num_list[0] == len(cards_to_score):
            score = 1
        elif card_num_list[0] == len(cards_to_score) - 1:
            score = 2
        elif card_num_list[0] == len(cards_to_score) - 2:
            if card_num_list[1] == 2:
                score = 3
            else:
                score = 4
        elif card_num_list[0] == len(cards_to_score) - 3:
            score = 6
        return score

    def __init__(self, card_info: list):
        self.cards = [card for card in card_info[0]]
        self.cards_subbed = [substitute_dict[card] for card in self.cards]
        self.bet = int(card_info[1])
        self.score = self.get_score_one(self.cards)
        self.cards_to_score = [card for card in self.cards if card != "J"]
        # If the length of the  list of cards to score with Jokers removed is 5, there are no Jokers and it can be scored the same as part one
        if len(self.cards_to_score) == 5:
            self.score_two = self.score
        else:
            self.score_two = self.get_score_two(self.cards_to_score)

        # Creates a new list of cards with the Joker replaced by N, the lowest ranking card in the substitute dictionary.
        self.cards_subbed_no_j = []

        for card in self.cards_subbed:
            if card != "D":
                self.cards_subbed_no_j.append(card)
            else:
                self.cards_subbed_no_j.append("N")


# Dict for reference / printing
score_dict = {
    1: "Five of a kind",
    2: "Four of a kind",
    3: "Full house",
    4: "Three of a kind",
    5: "Two pair",
    6: "One pair",
    7: "High card",
}
