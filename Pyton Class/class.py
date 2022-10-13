class Student:
    usn=23
    name='sumanth'
    branch='ise'
    def display(self):  #single argument which points to itself(self)
        print("Student class")
#Object

s1=Student()
print("The student usn=",s1.usn)
print("Branch is",s1.branch)
print("name",s1.name)


class Myclass():
    n=40
    a='abc'
    def myF(self):
        n=90
        print("this is function")
        print(n)
        print(self.n)
obj=Myclass()
print(obj.n)
obj.myF()

#constructor=initialise the variable
#destructor=it will be executed after constructor
#Constructor
print("__________________________________")
class Student:
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2

    def print(self):
        print("Num1 =",self.num1)
        print("Num2 =",self.num2)
s=Student(80,90)   #constructor
s.print()
print("__________________________________")

class Sample:
    def add(self,a,b):
        self.n1=a
        self.n2=b
        print("The sum of a and b is", self.n1+self.n2)
        
obj2=Sample()
obj2.add(20,30)

obj3=Sample()
obj3.add(10,20)
print("__________________________________")


class ISE:
    def Student(self,usn,name,age,marks):
        #local var
        self.usn=usn
        self.name=name
        self.marks=marks
        self.age=age
        print("The USN: {}, name: {}, age: {} and marks:{}".format(self.usn,self.name,self.age,self.marks))

s1=ISE()
s1.Student('is01','allen','22','99')
s2=ISE()
s2.Student('is02','Kiran','23','100')
print(s1.name)
print(s1.usn)
print(s1.marks)
print(s2.marks)
                                                                                                #Json->Mangodb









