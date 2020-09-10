"""
Program to Login to the Actitime webpage successfully

Scope:
1. Launch the Chrome browser
2. Navigate to Actitime Login page
3. Fill the Text fields Username, Password with the data respectively,
    click the "Keep me logged in" checkbox and click on the Login button
4. Actitime Home Page to be loaded successfully
5. Click on Add Recent Task dropdown to choose meetings
6. Quit the browser
"""

#Import Statement
import time
from selenium import webdriver

#Create an instance of Chrome Driver
browser= webdriver.Chrome()

#Navigate to the Actitime Login page
browser.get("https://demo.actitime.com/login.do")

#Check if the derived title is correct
if(browser.title=="actiTIME - Login"):
    print('Title derived successfully')
else:
    print("Failed to derive title")
time.sleep(2)

#Locate the Username field using "Xpath" locator with attribute "id"
Username= browser.find_element_by_xpath("//input[@name= 'username']")

#Insert data into the Username field
Username.send_keys('admin')
time.sleep(2)

#Locate the Password field using "Xpath" locator with attribute "class"
Password= browser.find_element_by_xpath("//input[@class= 'textField pwdfield']")

#Insert data into the Password field
Password.send_keys('manager')
time.sleep(1)

# Locate the checkbox "Id" locator
checkbox = browser.find_element_by_id("keepLoggedInCheckBox")
checkbox.click()

#Locate the Login button using "LinkText" locator
button= browser.find_element_by_link_text("Login")
button.click()
time.sleep(3)

#Locate the Reports tab using "LinkText" locator
Reports= browser.find_element_by_link_text("Reports")
Reports.click()
time.sleep(2)

#Locate the Dropdown right next to New Report using the "Id" locator
Dropdown= browser.find_element_by_id("ext-gen30")
Dropdown.click()
time.sleep(10)
 #Exit from the browser
browser.quit()
