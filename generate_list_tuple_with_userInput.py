def input_num_range():
    "Input sequence of numbers"
    num_seq= input("Enter the sequence of numbers separated by comas:")
    print(type(num_seq))
    return num_seq

def convert_to_list(num_seq):
    "Converting the sequence of numbers into a list"
    my_list= num_seq.split(',')
    print(my_list)
    print(type(my_list))
    return my_list

def convert_to_tuple(my_list):
    "Converting the sequence of numbers into a tuple"
    my_tuple=tuple(my_list)
    print(my_tuple)
    print(type(my_tuple))
    return my_tuple

if __name__=="__main__":
    num_seq= input_num_range()
    my_list= convert_to_list(num_seq)
    my_tuple=convert_to_tuple(my_list)