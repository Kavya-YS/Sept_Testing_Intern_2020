"""
Get the Formula for BMI calculation 
Formula: weight (kg) / [height (m)]2
Get the user inputs for weight in Kilogram and height in Metre
Calcualte the BMI using the formula and display the result
Validate with the BMI range and print the respective message

"""

weight=int(input("weight in Kg:"))
height = float (input("Height in metres"))
BMI= weight/(height*height)
round_BMI=round(BMI,2)
print("BMI is", round_BMI)
if BMI<=18.5:
    print("I am underweight")
elif BMI<=24.9:
    print("I am on a Healthy Weight range")
elif BMI<=29.9:
    print("I am overweight")
else:
    print("I am obese")