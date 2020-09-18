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

#Get the title of the page
if browser.title=="Current Temperature":
    print("Tittle of the home page is 'Current Temperature'")
else: 
    print("Unable to get title")

#Locate the temperature web application and print the temperature
temperature= browser.find_element_by_id("temperature").text
time.sleep(3)

#Splitting the string to get a list
dynamic_temperature= temperature.split(" ")

#Converting the String to an Integer
current_temperature=int(dynamic_temperature[0])

#Click on "Buy Moisturizers" button if the temperature is <=19 and click on "Buy Sunscreens" button if the temperature is >=34
if(current_temperature)<=19:
    buy_moisturizers= browser.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy moisturizers']").click()
    time.sleep(2)
    if browser.title=="The Best Moisturizers in the World!":
        print("The Best Moisturizers in the World!")
    else: 
        print("Unable to get Moisturizer page title")
elif current_temperature>=34:
    buy_sunscreens= browser.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy sunscreens']").click()
    time.sleep(2)
    if browser.title=="The Best Sunscreens in the World!":
        print("The Best Sunscreens in the World!")
    else: 
        print("Unable to get title")
else:
    print("No lotion required")
time.sleep(2)    
browser.quit()

