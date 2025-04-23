# class Student:
#     student_count = 0  # Class variable to track student count

#     def __init__(self, name, roll, age, percentage):
#         Student.student_count += 1
#         self.student_id = Student.student_count
#         self.name = name
#         self.roll = roll   
#         self.age = age
#         self.percentage = percentage

#     def greet(self):
#         print("\n\t--- Student Information ---")

#     def student_info(self):
#         print(f"ID: {self.student_id}\nName: {self.name}\nRoll: {self.roll}\nAge: {self.age}\nPercentage: {self.percentage}%\n")

# # Example Usage
# e1 = Student("Nishant", 51, 23, 83)
# e1.greet()
# e1.student_info()

# e2 = Student("Aditi", 52, 22, 90)
# e2.greet()
# e2.student_info()

class Emp:
    def __init__(self):     #constructor Employee
        self.e_name = 'Nish' #Instance Variables
        self.e_id = 51         #Instance variables
e1 = Emp()

print("Employee name for e1 is :",e1.e_name)
print("Employee name for e1 is :",e1.e_id)

e2 = Emp()

print("Employee name for e1 is :",e2.e_name)
print("Employee name for e1 is :",e2.e_id)