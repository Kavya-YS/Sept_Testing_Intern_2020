"""
Scope
1. Create an outer function and define the nolocal variables
2. create an inner function to modify nonlocal variables with the use of nonlocal keyword
3. Modify the nonlocal variables and also define the local variables within the function
4. Call the inner functions with respective print statements
5. Call the outer function
"""

#defining a function to declare nonlocal variables
def vehicles():
#Defining global variables
    wheel_base=1200
    ground_clearance=120
    
#Defining a function activa
    def activa():
        nonlocal wheel_base
        wheel_base= 1260
        nonlocal ground_clearance
        ground_clearance= 165
        fuel_tank_capacity=5.3 #local variable of activa() finction
        print("Activa's fuel_tank_capacity is: ", fuel_tank_capacity)
        
    def dio():
        nonlocal wheel_base
        wheel_base= 1270
        nonlocal ground_clearance
        ground_clearance= 171
        fuel_tank_capacity=4.5 #local variable of dio() finction
        print("Dio's fuel_tank_capacity is: ", fuel_tank_capacity)
            
    dio()
    print("Dio's wheel base is: ", wheel_base)
    print("Dio's ground clearance is: ", ground_clearance)
    activa()
    print("Activa's wheel base is: ", wheel_base)
    print("Activa's ground clearance is: ", ground_clearance)

vehicles()

