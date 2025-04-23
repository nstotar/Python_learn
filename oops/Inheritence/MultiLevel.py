class Animal:           #LEVEL 1
    def display(self):
        print("\nAnimals are too good")

class cat(Animal):      #Level 2
    def catLovers(self):
        print("Most of the girls like cats")

class Dog(cat):         #Level 3
    def DogLovers(self):
        print("Most of the boys like Dog\n")



o2 = Dog()
o2.display()
o2.catLovers()
o2.DogLovers()