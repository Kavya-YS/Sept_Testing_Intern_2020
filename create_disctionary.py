def user_input():
    number= int(input("Enter the number:"))
    return number

def create_dictionary(number):
    "create a dictionary with keys:i, (i*i)"
    this_dictionary={}
    for every_number in range(1, number+1):
        this_dictionary[every_number]= every_number*every_number
    print(this_dictionary)

if __name__=="__main__":
    number=user_input()
    create_dictionary(number)