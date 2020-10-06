class strGame():
    def __init__(self):
        self.str=""

    def getstr(self):
        "Get string through user input"
        self.str= input("Enter the string:")
        
    def printstr_up(self):
        "print the input string in upper case"
        self.upperstr= self.str.upper()
        print("string in upper case:", self.upperstr)

strGame_object1= strGame()
strGame_object1.getstr()
strGame_object1.printstr_up()

