
d={1,}
print(d)
print(type(d))

d={'usn':'2ba20is072', 'name':'manju','her_name':'Pragati'}
print(d)
print(type(d))

for i in d:
    print(d[i])


#adding elements inside the dictionary

#
# ##
d={'usn':'2ba20is072', 'name':'manju','her_name':'Pragati'}
d[4]=40
print(d)

#Update  element inside the dictionary
d={'usn':'2ba20is072', 'name':'manju','her_name':'Pragati'}
print(len(d))   #length
d['her_name']='Pragati g s'
print(d)

#new
d1={1:10,2:20,3:30}
d2={2:21,2:21}
d1.update(d2)
print(d1)

#deleting the elements from dictionary

'''
del statement
pop(key)
'''
#pop
d1={1:10,2:20,3:30}
d1.pop(2)
print(d1)

del d1
print(d1)