import random

# suits = (u"\u2664", u"\u2661", u"\u2662", u"\u2667")
# ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")


# Generate class Card (52 cards)
class Card:
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    @property
    def rank(self):
        return self.__rank

    @property
    def suit(self):
        return self.__suit


# Generate class Stack
class Stack:
    __stack = []

    @property
    def stack(self):
        return self.__stack

    def __init__(self, suits, ranks):
        self.__stack = [Card(i, j) for i in suits for j in ranks]
        random.shuffle(self.__stack)

    def __len__(self):
        return len(self.__stack)

    # Dealing card function
    def deal(self):
        return self.__stack.pop()

    # Print cards stack
    def __str__(self):
        result = ""
        for c in self.__stack:
            result += f"{c.suit}{c.rank} "
        return result


# Generate class Player
class Player:
    def __init__(self):
        self.__player = []

    @property
    def player(self):
        return self.__player

    # Getting a card from dealer function
    def get_card(self, card):
        return self.__player.append(card)

    # Print handing cards of player
    def __str__(self):
        on_hand = ""
        for c in self.__player:
            on_hand += f"{c.suit}{c.rank} "
        return on_hand


# if __name__ == '__main__':
#     stack = Stack()
#     players = [Player() for p in range(4)]
#
#     print(stack)
#     print(len(stack))
#
#     while len(stack) > 0:
#         for player in players:
#             oneCard = stack.deal()
#             player.get_card(oneCard)
#
#     for i in range(len(players)):
#         print(f"Player {i}: {players[i]}")
