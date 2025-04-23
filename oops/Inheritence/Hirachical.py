class Animal:
    def display(self):
        print("Animals are too good")
class cat(Animal):
    def catLovers(self):
        print("\nMost of the girls like cats")
class Dog(Animal):
    def DogLovers(self):
        print("\nMost of the boys like Dog")

obj1 = cat()
obj1.catLovers()
obj1.display()

o2 = Dog()
o2.DogLovers()
o2.display()