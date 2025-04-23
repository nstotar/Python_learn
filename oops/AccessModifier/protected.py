"""The Protected Variables must be accessed inside the same class or inside child class."""
class Demo:
    def __init__(self):
        self._name = 'Nishant' #Protected veriable
    def Disp1(self):
        print(self._name) #accessing inside the same class
d1= Demo()

class Demo2(Demo):
    def desp(self):
        print(self._name)  #Accessing inside child class
d2=Demo2()
