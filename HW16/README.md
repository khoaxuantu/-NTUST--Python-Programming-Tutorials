# Names that pass all courses and fail on all courses
 
<b>Description:</b>
- The scores of Math and History were stored as the following data structure:<br>
  table = {"Peter":(56, 75), "Jane":(68, 89), "Paul":(85, 44), "Robert":(87, 65), "Rola":(45, 58)}
- (The first score is Math, and the second score is History.)


<b>Hints:</b>
- Find all the names as the "Universal Set":<br>
  Names = {name for name in table.keys()}
- Find the names for who pass Math:<br>
  Math = {name for name, score in table.items() if score[0] >= 60}
- Find the names for who pass History:<br>
  History = {name for name, score in table.items() if score[1] >= 60}
- Use “Intersection” and “Complement” of sets to get the answer.
