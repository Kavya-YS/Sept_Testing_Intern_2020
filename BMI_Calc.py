"""
Get the Formula for BMI calculation 
Formula: weight (kg) / [height (m)]2
Get the user inputs for weight in KG and height in m
Calcualte the BMI using the formula and display the result

"""

weight=int(input("weight in Kg:"))
height = float (input("Height in metres"))
BMI= weight/(height*height)
round_BMI=round(BMI,2)
print("BMI is", round_BMI)