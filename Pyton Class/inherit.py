#singlelevel innheritance

class Parent:
    def pdisplay(self):
        print("Parent property")

class Child:
    def cdisplay(self):
        print("Childs property")

c1=Child()
c1.cdisplay()


class Parent:
    def pdisplay(self):
        print("Parent property")

class Child(Parent):
    def cdisplay(self):
        print("Childs property")

c1=Child()
c1.pdisplay()
print("____________________")
#multilevel inheritance

class GPClass:
    def gpdisplay(self):
        print("Grand Parent property!")
class ParentClass(GPClass):
    def pdisplay(self):
        print("Parent property!")
class ChildClass(ParentClass):
    def cdisplay(self):
        print("Child property!")

obj = ChildClass()
#obj.gpdisplay()
obj.cdisplay()
obj.pdisplay()
obj.gpdisplay()


#Hierarchical
print("__________________")
class Parent:
    def p1display(self):
     print("Parent Property!")

class Child1(Parent):
    def c1display(self):
        print("Child1 Diplay")

class Child2(Parent):
    def c2display(self):
        print("Child2 Diplay")

class Child3(Parent):
    def c3display(self):
        print("Child3 Diplay")

c1=Child1()
c1.p1display()
c1.c2display()

 

