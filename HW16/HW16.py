# Name student who pass or fail

# Table of transcript
# "name":(Math, History)
print("Transcript: ")
table = {"Peter": (56, 75), "Jane": (68, 89), "Paul": (85, 44), "Robert": (87, 65), "Rola": (45, 58)}
print(f"{table}\n")

# Classify all names
Names = {name for name in table.keys()}

# Classify who passes Math
Math = {name for name, score in table.items() if score[0] >= 60}

# Classify who passes History
History = {name for name, score in table.items() if score[1] >= 60}

# Find who passes both courses
print("Pass on both course:")
print(f"{Math & History}\n")

# Find who fails both courses
print("Fail on both course:")
print(f"{Names-History-Math}\n")
