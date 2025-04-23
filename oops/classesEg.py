class Student:
    roll_no = 51
    name = 'Nishant'
    def study(self): #for instence method self parameter is must 
        print("Student is studying")
    def code(self):
        print(f"coder is coding")
obj = Student()
obj2 = Student()
print(obj.name)
print(obj2.roll_no)
obj.study()
obj2.code()