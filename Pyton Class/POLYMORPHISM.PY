# IMPLEMENTING SAME METHOD IN DIFEERENT CONTEXT _______________________________________________
#WE CAN ACHIEVE THIS WITH THE HELP OF OVERRIDING AND OVERLOADING                               |
                                                                                            #   |    
'''
oPEREATOR  OVERLOADING->2 TYPES                                                                 |
                            + OPERATOR CAN ACT AS BOTH CONCATENATION AS WELL AS ADDITION  ________| 
                            also * operator used as multiplpication in integers as well as replicator in lists[]
METHOD OVERLOADING

'''
# n1='10'
# n2='20'
# print(n1+n2)

n1=[1,2,3,4]
print(n1*3)
#o/p
'''
PS C:\Users\omc\Music\Pyton Class> python -u "c:\Users\omc\Music\Pyton Class\POLYMORPHISM.PY"
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
PS C:\Users\omc\Music\Pyton Class>
'''
print("______________-")
#Method overloading

def add():
    n1=10
    n2=20
    summm=n1+n2
    print("Sum =",summ)

#call the function
add()