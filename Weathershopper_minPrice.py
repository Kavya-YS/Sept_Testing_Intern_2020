"""
Scope:
1. Navigate the Moisturizers page
2. List all the items in that page
3. select the least priced Moisturizer
4. Add it to the cart
"""

#Import Statement
import time
from selenium import webdriver
import re

#Create an instance of Chrome Driver
browser= webdriver.Chrome()

#Navigate to the weathershopper Moisturizer page
browser.get("http://weathershopper.pythonanywhere.com/moisturizer")

#Get title of the Moisturizers page
if browser.title=="The Best Moisturizers in the World!":
        print("The Best Moisturizers in the World!")

#Get details of each moisturizer details
moisturizers= browser.find_elements_by_xpath("//div[contains(@class, 'text-center col-4')]")
#print("Moisturizers: ", moisturizers)
for each_moisturizer in moisturizers:
    #print(each_moisturizer.text)
    time.sleep(2)
    moisturizer_details= each_moisturizer.text
    split_moisturizer_details= moisturizer_details.split('\n')
    #print("Split data is:", split_moisturizer_details)
    time.sleep(3)
    item_name=split_moisturizer_details[0]
    #print("product_name:", item_name)       
    item_price=split_moisturizer_details[1]
    #print("item_price:", item_price)
    #print(type(item_price))
    product_price= re.findall('\d+', item_price)
    #product_price= [int(each_price) for each_price in product_price]
    print("product_price are:", *product_price)
    print(type(product_price))
    time.sleep(2)
    product_name= item_name.split(',')
    #print("product_name is:", *product_name)   
    zipped_product_details= zip(product_name, product_price)
    #print("zipped_product_details:", zipped_product_details)
    product_details=list(zipped_product_details)
    print("product_details is:", *product_details)
    time.sleep(3)
    """min_price= []
    for price in product_details:
        if min_price < price:
            min_price = price
            print(min_price)"""
browser.quit()