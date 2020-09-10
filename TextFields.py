from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://qxf2.com/selenium-tutorial-main")
if(driver.title=="Qxf2 Services: Selenium training main"):
    print("Succesfully launched the Qxf2 training tutorial")
else:
    print("failed to launch the Qxf2 training tutorial")
name = driver.find_element_by_xpath("//input[@id='name']")
name.send_keys('Kavya_YS')
email= driver.find_element_by_xpath("//input[@type='email']")
email.send_keys('kavya.suryaprakash@qxf2.com')
Phone= driver.find_element_by_id('phone')
Phone.send_keys('9584365198')
time.sleep(3)
driver.close()