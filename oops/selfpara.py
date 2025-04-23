class Student:
    def study(self): #for instence method self parameter is must 
        print(f"{self.name} is studying")
    def code(self):
        print(f"roll no {self.roll_no} is coding")
obj = Student()
obj.roll_no = 51
obj.name = 'Nishant'
obj.study()
obj.code()

obj1 = Student()
obj1.roll_no = 56
obj1.name = 'Mrgeeky'
obj1.study()
obj1.code()