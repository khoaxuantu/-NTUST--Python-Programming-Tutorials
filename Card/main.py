# Dealing poker
import properties as p

# Set up suits and ranks for poker cards
suits = (u"\u2664", u"\u2661", u"\u2662", u"\u2667")
ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stack = p.Stack(suits, ranks)
    players = [p.Player() for player_num in range(4)]

    while len(stack) > 0:
        for player in players:
            oneCard = stack.deal()
            player.get_card(oneCard)

    for i in range(len(players)):
        print(f"Player {i+1}: {players[i]}")
