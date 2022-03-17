# Functions to implement with BMI

# BMI calculation
def BMI_calc(height, weight):

    return weight / pow(height/100, 2)


# BMI judge
def BMI_judge(BMI):
    if BMI < 18.5:
        print("Underweight")
    elif 18.5 <= BMI < 25:
        print("Normal weight")
    else:
        print("Overweight")
