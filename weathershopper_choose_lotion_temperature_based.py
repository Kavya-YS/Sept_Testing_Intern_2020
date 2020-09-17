"""
Scope:
1. Navigate to the weathershopper website
2. Get the title of the page
3. Determine the current temprature
4. Shop for moisturisers if the temperature is 19 degree and below. Shop sunscreens if the temprature is 34 and above
"""

#Import Statement
from selenium import webdriver
import time

#Create an instance of Chrome Driver
browser= webdriver.Chrome()

#Navigate to the weathershopper home page
browser.get("http://weathershopper.pythonanywhere.com/")

#Locate the temperature and print
temperature= browser.find_element_by_id("temperature").text
print("temperature:", temperature)
time.sleep(3)
dynamic_temperature= temperature.split(" ")
print("dynamic_temperature=", dynamic_temperature)
indices= [0]
current_temperature = [dynamic_temperature[index] for index in indices]
print(*current_temperature)

#select Moisturizers if the current_temperature is 19 degree and below
def checkforless(current_temperature, val1):
    val1=19
    for x in current_temperature:
        if val1 >= current_temperature:
            print("Buy Moisturizers")
        else:
            print("Buy Sunscreens")
browser.quit()
"""if (CheckForLess(current_temperature, val1)): print("Yes") 
else: print("No") 


if current_temperature<=19:
    print("Buy Moisturizers")
    #buy_moisturizers=browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
else: #current_temperature>=34:
    print("Buy Sunscreens")"""


