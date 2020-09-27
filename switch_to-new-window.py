"""
Scope:
1. Import Chrome driver
2. Navigate to the 1st window to be accessed
3. Get window hadles of 1st window
4. Get title of the 1st window
5. Get window handles of 2nd window
6. Switch to 2nd window and Navigate to the 2nd window
7. Get title of the 2nd window
8. Compare the title of window1 and window2 to make sure the switch has worked
9. Reroute back to the 1st window
10. Confirm if the control is switched back to 1st window by comparing their titles
11. Quite the browser
"""
import time
from selenium import webdriver
import site

#open the 1st window
driver= webdriver.Chrome()
driver.maximize_window()

#Navigate to the 1st window
driver.get("https://www.javatpoint.com/method-overriding-in-java")
driver.execute_script("window.open()")

#Get window handle of the 1st window
window_javaTpoint= driver.window_handles[0]

#Get title of the 1st window
window_javaTpoint_title= driver.title
print("Title of javaTpoint is:", window_javaTpoint_title)



#Get window handle of 2nd window
window_beginnersBook= driver.window_handles[1]

#Switch to the 2nd window
driver.switch_to.window(window_beginnersBook)

#Open 2nd window
driver.get("https://beginnersbook.com/2014/01/method-overriding-in-java-with-example/")


#Get the title of 2nd window
window_beginnersBook_title= driver.title
print("Title of BeginnersBook is:", window_beginnersBook_title)

#Compare and verify that the titles of parent window and child window doesn't match
if window_javaTpoint_title != window_beginnersBook_title:
    print("Control switched to BeginnersBook")
else:
    print("Control did not switch to BeginnersBook")
time.sleep(7)    
driver.switch_to.window(window_javaTpoint)
#Verify that the title now matches
if window_javaTpoint_title == driver.title:
    print('Back to the 1st window javaTpoint')
    print(driver.title)
print(quit)
driver.quit()    



 
