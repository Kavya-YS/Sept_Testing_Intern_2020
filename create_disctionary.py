def user_input():
    n= int(input("Enter value of n:"))
    return n


this_dictionary={}
def create_dictionary(n):
    "create a dictionary with keys:i, (i*i)"
    for i in range(1, n+1):
        this_dictionary[i]= i*i
    print(this_dictionary)





if __name__=="__main__":
    n=user_input()
    create_dictionary(n)