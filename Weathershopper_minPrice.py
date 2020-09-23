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
    time.sleep(2)
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

    # Mapping the product name from product_name list with its respective price in product_price list
    product_details= list(zip(product_name_list, product_price_list))
    print("product_details:", product_details)
    print(type(product_details))
    time.sleep(3)

    #product_price_list= [int(product_price) for product_price in range(len(product_price))]
    for product_price in product_price_list:
        for price in product_price:
            print("price:", price)
            price=int(price)
            print("Type of price:", type(price))
            # Iterating through the product_price to find the min-price of moisturizers
            min_price=0
            print("Type of min_price:", type(min_price))
            #for price in product_price:
            if int(price)<=int(min_price):
                min_price = price
                continue
            print("min_price: ", min_price)
                
browser.quit()
#for price in product price:
