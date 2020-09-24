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

product_name_list= []
product_price_list=[]

for each_moisturizer in moisturizers:
    print(each_moisturizer.text)
    #time.sleep(2)
    moisturizer_details= each_moisturizer.text
    split_moisturizer_details= moisturizer_details.split('\n')
    print("Split data is:", split_moisturizer_details)
    print(type(split_moisturizer_details))
    time.sleep(3)

    product_name=split_moisturizer_details[0]
    product_name_list.append(product_name)
    print("product_name_list is:", product_name_list)
    print(type(product_name_list))
    # Listing all the product price    
    product_price=split_moisturizer_details[1]
    #######product_price= product_price.split("Price: Rs. ")[-1] #[-1] points the last index in the list
    product_price= re.findall(r'\d+', product_price)
    product_price_list.append(product_price)
    print("product_price_list:", product_price_list)
    print(type(product_price_list))
    
    time.sleep(2)

    # Get product_details by mapping the product name from product_name list & price in product_price list
    product_details= list(zip(product_name_list, product_price_list))
    print("product_details:", product_details)
    print(type(product_details))
    time.sleep(3)
  #Get min_price traversing through
    min_price= product_price_list[0]
    for product_price in range(0, len(product_price_list), 1):
        min_price= min(min_price,product_price_list[product_price])
        print(min_price)
        print(type(min_price))
        index= product_price_list.index(min_price)
        print("index:", index)
        print(product_name_list[index])
        add_to_cart= browser.find_element_by_xpath("//button[contains(@onclick, 'addToCart')]").click()
        print("clicked on Add button")
        cart_items= browser.find_element_by_xpath("//button[contains(@class, 'thin-text nav-link')]").click()
        
