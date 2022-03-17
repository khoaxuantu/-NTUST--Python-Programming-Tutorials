# Deal Pokers
import random

# Set up poker cards
suits = ("♤", "♡", "♢", "♧")
ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
poker_card = [(i, j) for i in ranks for j in suits]

players = [[], [], [], []]

# Shuffle
random.shuffle(poker_card)
for i in range(len(poker_card)):
    poker_card[i] = ''.join(poker_card[i])

# Deal
turn = 0
while len(poker_card) > 0:
    for player in players:
        player.append(poker_card.pop(turn))

for player in range(len(players)):
    print(f"Player {player}: {players[player]}")
