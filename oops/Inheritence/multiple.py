class demo:
    def display(self):
        print("hello from Demo 1")

class demo2:
    def display2(self):
        print("hello from Demo 2")

class demo3(demo,demo2):
    def display3(self):
        print("hello from Demo 3")

c = demo3()
c.display3()
c.display2()
c.display()