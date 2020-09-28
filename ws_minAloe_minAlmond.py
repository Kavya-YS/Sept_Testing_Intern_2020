"""
Scope:
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
    
time.sleep(3)

#Get the list list of products containing Aloe essence
for  product_name in product_name_list:
    if sub_string_of_aloe in product_name:
        aloe_essence.append(product_name)
print("Aloe based moisturizers are:", aloe_essence)

#Get the list of prices for Aloe essence moisturizers
index_aloe_name= [product_name_list.index(item) for item in aloe_essence]
#print("index_aloe_name:", index_aloe_name)
aloe_price= [product_price_list[i] for i in index_aloe_name]
print("aloe_price:", aloe_price)

#Get minimum price of Aloe essence moisturizers
min_price_aloe= aloe_price[0]
for each_aloe_price in range(0, len(aloe_price), 1):
  min_price_aloe= min(min_price_aloe,aloe_price[each_aloe_price])
print("Minimum priced Aloe in the list:", min_price_aloe)


#Get the name of minimum priced Almond moisturizer
index_min_price_Aloe= aloe_price.index(min_price_aloe)
#print("Index of the minimum priced Aloe moisturizer:", index_min_price_Aloe)
print("Name of the minimum priced Aloe Moisturizer:", aloe_essence[index_min_price_Aloe])


#Add the minimum priced Aloe based moisturizer to the cart by clicking on the add button
aloe_add_to_cart= browser.find_element_by_xpath("//button[contains(@onclick, 'addToCart')]").click()

#Get the list list of products containing Almond essence
for  product_name in product_name_list:
    if sub_string_of_almond in product_name:
        almond_essence.append(product_name)
print("Almond based moisturizers are:", almond_essence)

#Get the list of prices for Almond essence moisturizers
index_almond_name= [product_name_list.index(item) for item in almond_essence]
#print("index_almond_name:", index_almond_name)
almond_price= [product_price_list[i] for i in index_almond_name]
print("almond_price:", almond_price)

#Get minimum price of Almond essence moisturizers
min_price_almond= almond_price[0]
for each_almond_price in range(0, len(almond_price), 1):
  min_price_almond= min(min_price_almond,almond_price[each_almond_price])
print("Minimum priced Almond in the list:", min_price_almond)

#Get the name of minimum priced Almond moisturizer
index_min_price_Almond= almond_price.index(min_price_almond)
#print("Index of the minimum priced Almond moisturizer:", index_min_price_Almond)
print("Name of the minimum priced Almond Moisturizer:", almond_essence[index_min_price_Almond])

#Add the minimum priced Almond based moisturizer to the cart byclicking on the add button
aloe_add_to_cart= browser.find_element_by_xpath("//button[contains(@onclick, 'addToCart')]").click()



#//button[contains(@onclick, 'addToCart(almond_essence[index_min_price_Almond], min_price_almond
#"//button[@onclick='addToCart(almond_essence[index_min_price_Almond], min_price_almond)']"
  


