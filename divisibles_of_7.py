def divisble_7():
    "Print numbers divisible by 7 and not divisible by 5"
    for num in range(1999, 3201):
        if num%7==0 and num%5!=0:
            print(num, end=',')
            

if __name__=="__main__":
    divisble_7()