
#Example : while installing we cannot see code , but only exe file,
#wE CANNOT CREATE OBJECT FOR ABSTRACT CLASS, WE HAVE TO USE ANOTHER CONCRETE CLASS

from abc import ABC, abstractmethod
#abstract class
class AbstractDemo(ABC):
    #abstract method
    @abstractmethod
    def display(self):
        None
class BaseClass(AbstractDemo):
    def display(self):
        print('THis is Abstract function')
obj=BaseClass()
obj.display()
