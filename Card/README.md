# Poker Dealing with OOP
 
## Purpose:
- Generate a deck of pokers and deal to 4 players randomly.
- Please use Object-Oriented Programming Style to implement this project.
- The output should look like the attached image file.


## Hints:
- 52 Cards → class Card

  Property：suit → Read & Write
  
  Property：rank → Read & Write
  
- 1 Card Stack → class CardStack = 52 x Card Objects

  __init__: Generate 52 x Card object and .shuffle them.

  deal()：Draw and deal a card for users.
  
- 4 Players → class Player

  __init__: Generate an empty list to store 13 cards.

  getCard(oneCard): Accept one card object.

  __str__: Print all the 13 cards of this player.
  
- main.py
  Generate a CardStack object.

  Generate 4 objects of class Player

  Use .deal() return one card and use .getCard() to deal for a player.
  
  Print 4 players with class Player’s __str__ function.
