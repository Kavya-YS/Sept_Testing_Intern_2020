"""Scope:
1. Navigate the Moisturizers page
2. Prepare the list of product names and product price seperately
3. Merge the product names and their respective product price into product details
4. Check the condition for min priced product
5. Retrieve the product price, its index and product name from the list and print it
6. Click on Add button

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
sub_string_of_aloe= "Aloe"
aloe_essence=[]
aloe_price=[]
sub_string_of_almond= "Almond"
almond_essence=[]
almond_price=[]

for each_moisturizer in moisturizers:
  #print(each_moisturizer.text)
  moisturizer_details= each_moisturizer.text
  split_moisturizer_details= moisturizer_details.split('\n')
  #print("Moisturizer details are:", split_moisturizer_details)
  time.sleep(3)

  product_name=split_moisturizer_details[0]
  product_name_list.append(product_name)
  #print("product_name_list is:", product_name_list)
  # Listing all the product price
  product_price=split_moisturizer_details[1]
  product_price= re.findall(r'\d+', product_price)
  product_price_list.append(product_price)
  #print("product_price_list:", product_price_list)

  # Get product_details by mapping the product name from product_name list & price in product_price list
  product_details= list(zip(product_name_list, product_price_list))
print("product_details:", product_details)

#Get the list of products containing Aloe essence
for  product_name in product_name_list:
    if sub_string_of_aloe in product_name:
        aloe_essence.append(product_name)
print("Aloe_based_moisturizers_list:", aloe_essence)

#Get the list of prices for Aloe essence moisturizers
index_aloe_name= [product_name_list.index(item) for item in aloe_essence]
#print("index_aloe_name:", index_aloe_name)
aloe_price= [product_price_list[i] for i in index_aloe_name]
print("aloe_price_list:", aloe_price)

#Getting the least priced Aloe moisturizer, print its name and price
min_price_aloe=min(aloe_price)
index_min_price_aloe=aloe_price.index(min_price_aloe)
min_price_aloe=min_price_aloe[0]
min_aloe_name= aloe_essence[index_min_price_aloe]
min_aloe_name="'"+min_aloe_name+"'"
print("min_price_aloe, min_aloe_name:", min_price_aloe, min_aloe_name)

#Clicking on the Add button of minimum priced Aloe based moisturizer
browser.find_element_by_xpath('//button[@onclick="addToCart(%s,%s)"]'%(min_aloe_name, str(min_price_aloe))).click()


#Get the list of products containing Almond essence
for  product_name in product_name_list:
    if sub_string_of_almond in product_name:
        almond_essence.append(product_name)
print("Almond_based_moisturizers_list:", almond_essence)

#Get the list of prices for Almond essence moisturizers
index_almond_name= [product_name_list.index(item) for item in almond_essence]
#print("index_almond_name:", index_almond_name)
almond_price= [product_price_list[i] for i in index_almond_name]
print("almond_price_list:", almond_price)

#Getting the least priced Almond moisturizer, print its name and price
min_price_almond=min(almond_price)
index_min_price_almond=almond_price.index(min_price_almond)
min_price_almond=min_price_almond[0]
min_almond_name= almond_essence[index_min_price_almond]
min_almond_name="'"+min_almond_name+"'"
print("min_price_almond, min_almond_name:", min_price_almond, min_almond_name)

#Clicking on the Add button of minimum priced Aloe based moisturizer
browser.find_element_by_xpath('//button[@onclick="addToCart(%s,%s)"]'%(min_almond_name, str(min_price_almond))).click()