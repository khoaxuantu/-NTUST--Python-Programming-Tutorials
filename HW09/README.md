# Throw Divination Blocks
 
<b>Description:</b>
- It is the way to seek answers from God used by most of Taiwanese temples.
- Write a program to simulate the process of throwing divination blocks, until “Yes” was shown.
- Generate 2 random numbers, block1 & block2, to represent two divination blocks.
- Print different messages corresponding to different combinations:
  > one round + one flat → print “Yes (1, 0)” or “Yes (0, 1)”<br>
  > two round → print “No (1, 1)”<br>
  > two flat → print “Unclear (0, 0)”.
- Your program should also show how many counts of throwing until “Yes” has happened.
- This homework will test your skills of random numbers, branches, loops, and break command.
- The output should be looks like the attached image.


Hints:
- To generate a random number either 0 or 1
  > block = random.randint(0, 1)
- To count the throwing times until “YES” was happened
  > count = 0;<br>
  > Right after you generate random numbers once, count += 1<br>
  > Print the number of count at the last step of simulation.
- How to check the combination is “YES”, “NO”, or “UNCLEAR”?
  > Use if … elif … else …
