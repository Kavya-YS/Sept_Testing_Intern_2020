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
    print(each_moisturizer.text)
    time.sleep(2)
    moisturizer_details= each_moisturizer.text
    split_moisturizer_details= moisturizer_details.split('\n')
    print("Split data is:", split_moisturizer_details)
    
    time.sleep(3)

    #listing all the product names
    product_name=split_moisturizer_details[0]
    print("product_name:", product_name)
    print(type(product_name))

    # Listing all the product price    
    product_price=split_moisturizer_details[1]
    #product_price= product_price.split("Price: Rs. ")[-1] #[-1] points the last index in the list
    #print(type(item_price))
    product_price= re.findall('\d+', product_price)
    product_price= [int(each_price) for each_price in product_price]
    print("product_price:", product_price)
    print(type(product_name))
    time.sleep(2)

    # Mapping the product name from product_name list with its respective price in product_price list
    product_details= map(list, zip(product_name, product_price))
    #print("zipped_product_details:", *zipped_product_details)
    #product_details=list(zipped_product_details)
    #print("product_details is:", end="")
    print("product_details:", list(product_details))
    time.sleep(3)

    # Iterating through the product_price to find the min-price of moisturizers
    """
    min_price= 0
    product_price=int(product_price)
    print("converted product_price:", product_price)
    print(type(product_price))
    for each_price in product_price:
        if min_price < each_price:
            print(type(each_price))
            min_price = each_price
            print(min_price)
browser.quit()"""