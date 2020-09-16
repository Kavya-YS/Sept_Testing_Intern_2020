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

#Check if the derived title is correct
if(browser.title=="Current Temperature"):
    print("Welcome to weathershopper")
else:
    print("Failed to get title")

#Locate the Current temperature and print
#temperature= browser.find_elements_by_id("temperature")
temperature= browser.find_element_by_xpath("//*[@id='temperature']")
print("temperature= ", temperature)
time.sleep(3)
browser.quit()
