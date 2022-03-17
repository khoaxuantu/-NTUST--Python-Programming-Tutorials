# Calculate BMI
from BMIFunctions import BMI_calc, BMI_judge

# Input height, weight
height = int(input("Please enter your height (cm): "))
weight = int(input("Please enter your weight (kg): "))

# Calculate BMI
BMI = BMI_calc(height, weight)

# Judge the BMI
BMI_judge(BMI)
