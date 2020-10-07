import math
class Squareroot():
    def __init__(self):
        self.constantA= 50
        self.constantB= 30
         
    def input_variable(self):
        "Taking the variable value of var1 in series through user input"
        self.var1= input("Enter the coma separated inputs for var1:")
        return self.var1

    def convert_to_list(self):
        "Converting the above series of input from string to list"
        self.var1_list= list((self.var1).split(","))
        print(self.var1_list)
               
    def formula_calc(self):
        "Calculating the square root using below formula and print the result for series of d value"
        self.result=[]
        for each_num in self.var1_list:
            self.result = math.sqrt((2 * self.constantA * int(each_num))/self.constantB)
            self.result= round(self.result)
            print(self.result, end=" ")  
    
if __name__ == "__main__":
    Squareroot_obj= Squareroot()
    Squareroot_obj.input_variable()
    Squareroot_obj.convert_to_list()
    Squareroot_obj.formula_calc()



    