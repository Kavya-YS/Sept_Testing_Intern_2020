"""
Scope
1. Define the global variables outside the function
2. Create a function to define its respective local variables and modify the global variable using global keyword
3. call the function to print and view the changes
"""
order_no= input("Order no is:")
order_placed_date= input("Order placed Date is:")
shipping_address= "#56, 2nd cross, Nagappa Street, Palace Guttahalli, Bangalore-560003"
print("Shipping Address is:", shipping_address)
total_item= int(input("Total items are:"))
   
#Defining the the function item_info that hold the item details
def item_info():
    global shipping_address  #global keyword implementation
    shipping_address= "#25, 5th cross, P&t Layout, Horamavu, Bangalore-43"
    print("Changed Shipping Address is:", shipping_address)
    item_name= input("Item Name:")
    print(item_name)
    quantity= int(input("Quantity:"))
    print(quantity)
    price=int(input("Price:"))
    price_as_per_quantity= price*quantity
    print("price as per quantity:", price_as_per_quantity)
    
#Calling the item_info function
for x in range(total_item):
    item_info()
    