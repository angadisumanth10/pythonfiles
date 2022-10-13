t=('apple','mango','grapes')
if 'apple' in t:
    print("true")
print("False")
print("____________________")
#comparing of tuples

t1=(10,20,30)
t2=(10,20,30)
t3=(89,89)

print(t1 ==t2)
print(t1==t3)

#Min (tuple)
t1=(10,20,30)
print(min(t1))
print(max(t2))

#count
t1=(10,20,30,30)
print(t1.count(30))

#delete the statement

t1=(10,20,30)
del t1
print(t1)