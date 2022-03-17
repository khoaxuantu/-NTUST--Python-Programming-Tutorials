# Transcript DNA to RNA
import sys

# Input a DNA sequence
DNA = input("Enter the DNA sequence: ")
DNA_ls = list(DNA.upper())

# Transcript to RNA
for i in range(len(DNA_ls)):
    if DNA_ls[i] not in 'ATGC':
        sys.exit("Invalid DNA symbol(s)!")
    else:
        if DNA_ls[i] == 'A':
            DNA_ls[i] = 'U'
        elif DNA_ls[i] == 'T':
            DNA_ls[i] = 'A'
        elif DNA_ls[i] == 'G':
            DNA_ls[i] = 'C'
        elif DNA_ls[i] == 'C':
            DNA_ls[i] = 'G'

RNA = "".join(DNA_ls)
print(f"RNA: {RNA}")
