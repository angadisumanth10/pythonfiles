#Public class of encapsulation
class EncapClass:
    a=10
    def encapFun(self):
        print("This is Encapsulation function")
obj=EncapClass()
print(obj.a)
obj.encapFun()

#private
class EncapClass:
    __a=10
    def encapFun(self):
        print("This is Encapsulation function")
        print(self.__a)
obj=EncapClass()
obj.encapFun()