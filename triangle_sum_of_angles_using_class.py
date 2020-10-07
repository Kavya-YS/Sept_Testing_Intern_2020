class Triangle():
    def __init__(self, angle1, angle2, angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
        self.number_of_sides=3
        self.my_triangle=0

    def check_angles(self):
        self.flag= False
        self.sum_of_angles= self.angle1 + self.angle2 + self.angle3
        if self.sum_of_angles==180:
            self.flag = True
        else:
            print("sum_of_angles not within the range")


    def display(self):
        print("angle1:", self.angle1)
        print("angle2:", self.angle2)
        print("angle3:", self.angle3)
        print("sum_of_angles:", self.sum_of_angles)
       

if __name__ == "__main__":
    Triangle_object1= Triangle(40, 120, 60)
    Triangle_object1.check_angles()
    Triangle_object2= Triangle(90,30,60)
   
   
    Triangle_object1.display()