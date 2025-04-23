class Employee:
    id = 0      #class veriable
    def __init__(self,name):
        Employee.id+=1
        self.name=name
        self.id = Employee.id
e1 = Employee('NIshant')
e2 = Employee("Shin")

print(f"\t Emp1 object \n\nEmployee Name:{e1.name}\nEmployee Id:{e1.id} \n")
print(f" \t Emp2 object \n\nEmployee Name:{e2.name}\nEmployee Id:{e2.id}\n")

print("\n\n\n")




# Example

class Student:
    def __init__(self,name,id):
        self.name=name
        self.id = id
    def learn(self):
        print(f"{self.name} is learning")
    def Play(self):
        print(f"Student with id: {self.id} is playing")
    def display(self):
        print(f"\nName:{self.name}\nId:{self.id}")
s1 = Student('Ak',101)
s2 = Student("Pk",102)
s3 = Student('Rk',103)

s1.display()
s1.learn()
s1.Play()

s2.display()
s2.learn()
s2.Play()

s3.display()
s3.learn()
s3.Play()