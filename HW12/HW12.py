# Calculate and store the length of each person name using tuple
strings = tuple(input("Input comma seperated names: ").split(', '))

name_length = ((s, len(s)) for s in strings)

print(tuple(name_length))
