# Request a year
year = int(input("Please input a year: "))

# Check if it is leap year or not
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is regular year")
