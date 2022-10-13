S={}
s=set(S)
print(type(s))


s={2,2,4,5,6}
print(s)

l=[1,2,3,4]
l=set(l)
print(l)
print("_______")
#traverse set
s={2,2,4,5,6}
for i in s:
    print(i, end=' ')
    # to access the elements
    #we cannot acess but we can traverse
    print("\n")
print(s)
print(len(s))


#to add new element inside the set

s={10,20,30}
s.add(55)
print(s)

#update elements
s1={10,20,30}
s2={20,30}
s1.update(s2)
print(s1)

s1.remove(20)
print(s1)

s2={10,20,30,40,50}
s2.pop()
print(s2)
print(id(s2))

s2.discard(10)
print(s1)
print("______________")
s1={1,2,3,4,5,6}
s2={7,8,9}
print(s1.union(s2))

#intersection
print("______________")
s1={1,2,3,4,5,6}
s2={7,8,9,3}
print(s1.intersection(s2))
print("______________")

print(s1 - s2)