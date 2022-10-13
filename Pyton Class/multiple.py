#Multiple Inheritance

class Father:
    def f1display(self):
        print("Fathers property")

class Mother:
    def m1display(self):
        print("Motherss property")

class Childd(Father,Mother):
    def c3display(self):
        print("Child property")

c=Childd()
c.f1display()
c.m1display()
c.c3display()

#Android
#Automation testing
#VR