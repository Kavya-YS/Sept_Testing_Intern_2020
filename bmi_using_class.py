class Bmi():
    def __init__(self):
        self.height= 0
        self.weight= 0

    def bmi_input(self):
        "Input the height and weight"
        self.height= float(input("height in m:"))
        self.weight= float(input("weight in kg:"))
        return self.height, self.weight

    def bmi_calc(self):
        self.bmi= self.weight/(self.height*self.height)
        self.round_bmi=round(self.bmi,2)
        print(self.round_bmi)
        return self.round_bmi

    def bmi_range(self):
        if self.round_bmi<=18.5:
            print("I am underweight")
        elif self.round_bmi<=24.9:
            print("I am on a Healthy Weight range")
        elif self.round_bmi<=29.9:
            print("I am overweight")
        else:
            print("I am obese")

Bmi_object=Bmi()
Bmi_object.bmi_input()
Bmi_object.bmi_calc()
Bmi_object.bmi_range()