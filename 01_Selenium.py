"""
Program to Navigate to a particular URL successfully

Scope:
1. Launch the Chrome browser
2. Navigate to the Factoriall page
3. Derive page tittle
4. Close the browser
"""
#Import Statement
from selenium import webdriver

#Create an instance of Chrome browser
browser= webdriver.Chrome()

#Navigate to the Factoriall page
browser.get('http://qainterview.pythonanywhere.com/')

#Check if the title of the page is proper
if(browser.title=='Factoriall'):
    print('Successfully derived the tittle of Factoriall page')
else:
    print('Failed to grab the tittle from Factoriall page')
       
    #Quit browser
     browser.quit()