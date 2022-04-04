# Poker Dealing with OOP
 
## Purpose:
- Generate a deck of pokers and deal to 4 players randomly.
- Please use Object-Oriented Programming Style to implement this project.


## Hints:
- 52 Cards → class Card<br/>
  Property：suit → Read & Write<br/>
  Property：rank → Read & Write
  
- 1 Card Stack → class CardStack = 52 x Card Objects<br/>
  __init__: Generate 52 x Card object and .shuffle them.<br/>
  deal()：Draw and deal a card for users.
  
- 4 Players → class Player<br/>
  __init__: Generate an empty list to store 13 cards.<br/>
  getCard(oneCard): Accept one card object.<br/>
  __str__: Print all the 13 cards of this player.
  
- main.py<br/>
  Generate a CardStack object.<br/>
  Generate 4 objects of class Player<br/>
  Use .deal() return one card and use .getCard() to deal for a player.<br/>
  Print 4 players with class Player’s __str__ function.
