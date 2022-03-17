# Request a number
n = int(input("Please input a number n (n >= 0): "))

# Calculate factorial of n
factorial = 1
if n < 0:
    print("Error: Input number should be >= 0")
elif n == 0 or n == 1:
    print(f"{n}! = 1")
else:
    for i in range(1, n+1):
        factorial *= i
    print(f"{n}! = {factorial}")
