from selenium import webdriver
browser= webdriver.Chrome()
browser.get('http://qainterview.pythonanywhere.com/')
if(browser.title=='Factoriall'):
    print('Successfully derived the tittle of Factoriall page')
else:
    print('Failed to grab the tittle from Factoriall page')
    browser.quit()