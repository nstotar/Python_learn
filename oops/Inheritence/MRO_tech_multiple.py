class Demo1:
    def Magic(self):
        print("Magic method From Demo1 class")

class Demo2:
    def Magic(self):
        print("Magic method from Demo2 class")

class Demo3(Demo1,Demo2):
     pass

o = Demo3()
o.Magic()
print(Demo3.__mro__)  
# MRO technique is used to find the methods in multiple inheritence


class Demo1:
    def __init__(self):
        self.x = 100

class Demo2:
    def __init__(self):
        self.x=200

class Demo3(Demo1,Demo2):
     pass

o = Demo3()
print(o.x)

# output is 100  Because the x value will be choosen
#  from Demo1 class as it appears in 1st position in Demo3(Demo1,Demo2) 
# Method Resolution Order(MRO) SEQUENCE [ Demo3--->Demo1--->Demo2 ] 