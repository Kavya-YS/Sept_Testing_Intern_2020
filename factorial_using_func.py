import math

def user_input():
    "Input the number for calculating factorial"
    num= int(input("Enter an integer:"))
    return num

def factorial_calc(num):
    "Calculate the factorial for the range of numbers from the user input"
    for num in range(num):
        fact_num=math.factorial(num)
        print(fact_num, end=', ')

if __name__=="__main__":
    num= user_input()
    factorial_calc(num)

