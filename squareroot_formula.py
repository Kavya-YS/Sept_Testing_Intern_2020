import math
class Squareroot():
    def __init__(self):
        self.c= 50
        self.h= 30       

    def input_variable(self):
        "Taking the variable value of d in series through user input"
        self.d= int(input("Enter the coma separated inputs for d:"))
        return self.d

    def formula_calc(self):
        "Calculating the square root using the formula and print the resultfor series of d value"
        #for each_integer in self.d:
        self.result = math.sqrt((2 * self.c * self.d)/self.h)
        self.result= round(self.result)
        print("result is:", self.result)
    
if __name__ == "__main__":
    Squareroot_obj= Squareroot()
    Squareroot_obj.input_variable()
    Squareroot_obj.formula_calc()

    