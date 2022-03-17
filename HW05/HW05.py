# Input height, weight
h = int(input("Please input your height(cm): "))
w = int(input("Please input your weight(kg): "))

# Calculate BMI
BMI = w/pow(h/100, 2)

# Judge the BMI
if BMI < 18.5:
    print("Underweight")
elif BMI >= 25:
    print("Overweight")
else:
    print("Normal weight")
