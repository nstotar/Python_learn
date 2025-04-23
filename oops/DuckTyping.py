class Add:
    def calculate(self,a,b):
        print(a+b)
class Mul:
    def calculate(self,a,b):
        print(a * b)
class Div:
    def calculate(self,a,b):
        print(a / b)

def permit(ref):
    ref.calculate(10,20)
    
permit(Add())
permit(Mul())
permit(Div())

class car:
    def max_speed(self):
        print("Car max speed is 180 km/h")
class Cheeta:
    def max_speed(self):
        print("Cheetah capable of reaching speeds as high as 75 mph or 120 km/h")

def difClasButSameMethod(obj):
    obj.max_speed()
difClasButSameMethod(car()) #car class
difClasButSameMethod(Cheeta()) #cheetah class