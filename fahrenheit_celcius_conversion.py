class Temperature():
    def __init__(self, celcius, fahrenheit):
        self.celcius=celcius
        self.fahrenheit= fahrenheit

    def convert_Fahrenheit(self):
        self.fahrenheit=((self.celcius * 9)/5) + 32
        print("Temperature in fahrenheit:", self.fahrenheit)

    def convert_celcius(self):
        self.celcius= ((self.fahrenheit - 32) * 5)/9
        print("Temperature in celcius:", self.celcius)

temp_obj= Temperature(120, 380)
temp_obj.convert_Fahrenheit()
temp_obj.convert_celcius()


        

