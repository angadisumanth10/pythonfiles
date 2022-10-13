'''
class
different class but same name of methods
Integrating test

'''

class Parent:
    a=10
    def display(self):
        print("Parent proprty")

class Child(Parent):
    a=30
    def display(self):
        print("Child Property")

c=Child()
print(c.a)
c.display()


