"""
Program to insert valid data into Text fields

Scope:
1. Launch the Chrome browser
2. Navigate to Qxf2 Selenium Tutorial page
3. Fill the Text fields Name, Email ID and Phone Number with the data respectively
4. Close the browser
"""
#Import Statement
from selenium import webdriver

#Create an instance of Chrome Driver
driver = webdriver.Chrome()

#Navigate to the Qxf2 Selenium Tutorial page
driver.get("http://qxf2.com/selenium-tutorial-main")

#Check if the derived title is correct
if(driver.title=="Qxf2 Services: Selenium training main"):
    print("Succesfully launched the Qxf2 training tutorial")
else:
    print("failed to launch the Qxf2 training tutorial")

#Locate the name field using Xpath locator with "id" attribute
name = driver.find_element_by_xpath("//input[@id='name']")

#Insert data into the name field
name.send_keys('Kavya_YS')

#Locate the email field using Xpath locator with "Type" attribute
email= driver.find_element_by_xpath("//input[@type='email']")

#Insert data into the email field
email.send_keys('kavya.suryaprakash@qxf2.com')

#Locate the name field using Id locator
Phone= driver.find_element_by_id('phone')

#Insert data into the Phone field
Phone.send_keys('9584365198')
time.sleep(3)

#Close the browser
driver.close()