def user_input():
    n= int(input("Enter value of n:"))
    return n



def create_dictionary(n):
    "create a dictionary with keys:i, (i*i)"
    for i in range(n):
        this_dictionary= {"n": i, "n*n": i*i}
        print(this_dictionary)





if __name__=="__main__":
    n=user_input()
    create_dictionary(n)