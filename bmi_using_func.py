def bmi_input():
    "Input the height and weight"
    height= float(input("height in m:"))
    weight= float(input("weight in kg:"))
    return height, weight
    

def bmi_calc(height, weight):
    bmi= weight/(height*height)
    round_bmi=round(bmi,2)
    print(round_bmi)
    return round_bmi

def bmi_range(round_bmi):
    if round_bmi<=18.5:
        print("I am underweight")
    elif round_bmi<=24.9:
        print("I am on a Healthy Weight range")
    elif round_bmi<=29.9:
        print("I am overweight")
    else:
        print("I am obese")



if __name__=="__main__":
    height, weight=bmi_input()
    round_bmi= bmi_calc(height, weight)
    bmi_range(round_bmi)
