class Lunch():
    def __init__(self, menu):
        self.menu=menu
        
    def menu_price(self):
        "Displaying the menu chosen and its respective Price"
        if self.menu== "menu1":
            print("Your choice:", self.menu, "Price 12.00")
        elif self.menu== "menu2":
            print("Your choice:", self.menu, "Price 13.40")
        else:
            print("Error in menu")

Lunch_paul= Lunch("menu1")
Lunch_paul.menu_price()