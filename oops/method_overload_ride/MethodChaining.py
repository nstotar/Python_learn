class GreatGrandParent:
    def cook(self):
        print("Great grand parent is Cooking")

class GrandParent(GreatGrandParent):
    def cook(self):
        print("Grand Parents cook")

class Parent(GrandParent):
    def cook(self):
        print("Parents is Cook")

class child(Parent):
    def cook(self):
        print("child is cooking")
        super().cook()
        super(Parent,self).cook()
        super(GrandParent,self).cook()

c1= child()
c1.cook()





