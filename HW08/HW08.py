# Make a Multiplication Table
for i in range(1, 10):
    for j in range (1, 10):
        multi = i * j
        print("{:2d} x{:2d} = {:2d}".format(j, i, multi), end=" ")
    print()
