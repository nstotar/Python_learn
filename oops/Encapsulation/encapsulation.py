class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    def set_age(self,newAge):
        self.__age = newAge
p = Person("Ravi",23)
print(p.name)
print(p.get_age())
p.set_age(33)
print("after updating age ",p.get_age())