h = int(input("Please input your height(cm): "))
w = int(input("Please input your weight(kg): "))

# BMI calculation = (height/weight)^2
BMI = w/pow(h/100, 2)

print("Your BMI = {:.2f}".format(BMI))
