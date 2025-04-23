class base:
    def display(self):
        print("hello from base class")
class derived(base):
    def disp(self):
        print("hello from derived class")
e1 = derived()
e1.display()
e1.disp()