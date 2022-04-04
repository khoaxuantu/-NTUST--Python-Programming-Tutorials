# Write a Program to Deal Pokers
 
<b>Purpose:</b>
- Generate a deck of pokers and deal to 4 players randomly.
- The execution result should look like the attached image.


<b>Hints:</b>
- To generate 52 cards:<br>
  suits = ("♤", "♡", "♢", "♧")<br>
  ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")<br>
  pokers = [(i, j) for i in suits for j in ranks]
- To generate 4 players:<br>
  players = [[], [], [], []] → players[0] = [], players[1] = [], … players[3] = []
- To shuffle 52 cards:<br>
  import random
  random.shuffle(pokers)
- Deal a card from the Stack until it is empty:<br>
  while len(pokers) > 0:<br>
  Use .pop() to deal a card to players.
- Print Cards owned by Players<br>
  Use for card in players[i]: to literate one card like (‘♡’, ‘A‘) of player i.<br>
  Use “”.join(card) can print a tuple (‘♡’, ‘A‘) as a string like this: “♡A”.
