print("DEMO3---->Demo2--->Demo1--->Object")

class Demo1:
    def __init__(self):
        self.x=100

class Demo2:
    def __init__(self):
        self.x=200   
        super().__init__()
class Demo3(Demo2,Demo1):
    pass

obj  = Demo3()
print(obj.x)

print("DEMO3---->Demo1--->Demo2--->Object")

class Demo1:
    def __init__(self):
        self.x=100
        super().__init__()
class Demo2:
    def __init__(self):
        self.x=200   
        super().__init__()
class Demo3(Demo1,Demo2):
    pass

obj  = Demo3()
print(obj.x)