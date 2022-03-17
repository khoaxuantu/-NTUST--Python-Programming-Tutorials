# Throw Divination Blocks
import random

count = 0
while True:
    # Generate random numbers
    block1 = random.randint(0, 1)
    block2 = random.randint(0, 1)

    # Check the combinations
    if not (not block1 or not (block2 == 1)):
        print(f"No ({block1}, {block2})")
        count += 1
    elif block1 == 0 and block2 == 0:
        print(f"Unclear ({block1}, {block2})")
        count += 1
    else:
        print(f"Yes ({block1}, {block2})")
        count += 1
        break
print(f"It takes {count} times to get YES!")