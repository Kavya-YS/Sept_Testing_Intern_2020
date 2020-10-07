"""
Program to Login to the Actitime webpage successfully

Scope:
1. Launch the Chrome browser
2. Navigate to Actitime Login page
3. Fill the Text fields Username, Password with the data respectively,
    click the "Keep me logged in" checkbox and click on the Login button
4. Actitime Home Page to be loaded successfully
5. Click onReports tab and click on the drop down "New Report"
6. choose the Leave Time and Balance option and navigate to that url
7. Confirm if the user has landed on the correct url
8. Quit the browser
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
Password= browser.find_element_by_xpath("//input[@name= 'pwd']")

#Insert data into the Password field
Password.send_keys('manager')
time.sleep(1)

# Locate the checkbox "Id" locator
checkbox = browser.find_element_by_id("keepLoggedInCheckBox")
checkbox.click()

#Locate the Login button using "Xpath" locator with attribute "id"
button= browser.find_element_by_xpath("//a[@id='loginButton']")
button.click()
time.sleep(3)

#Locate the Reports tab using "Xpath" locator with tect() function
Reports= browser.find_element_by_xpath("//a[contains(@class, 'reports')]")
Reports.click()
time.sleep(2)

#Locate the Dropdown right next to New Report using the "Id" locator
Dropdown= browser.find_element_by_id("ext-gen30")
Dropdown.click()

#Locate the Leave Time and Balance option and navigate to the respective page
leave_time_balance= browser.find_element_by_xpath("//a[@href='/reports/leaves.do']").click()
time.sleep(2)

#Comparing the current url with the desired url to be landed anddisplay the respective message
current_url=browser.current_url
print(current_url)
if current_url== "https://demo.actitime.com/reports/leaves.do":
    print("Landed on the correct url")
else:
    print("wrong url")
 #Exit from the browser
browser.quit()
