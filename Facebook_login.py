import time
from selenium import webdriver
browser= webdriver.Chrome()
browser.get("https://demo.actitime.com/login.do")
"""if(browser.title=="actiTIME - Login"):
    print('Title derived successfully')
else:
    print("Failed to derive title")
time.sleep(2)"""
Username= browser.find_element_by_xpath("//input[@name= 'username']")
Username.send_keys('admin')
time.sleep(2)
Password= browser.find_element_by_xpath("//input[@class= 'textField pwdfield']")
Password.send_keys('manager')
time.sleep(1)
button= browser.find_element_by_link_text("Login")
button.click()
time.sleep(10)
browser.quit()
