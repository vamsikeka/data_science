import numpy as np

#as a list slicing
a = [6,7,8]
print(a[0:2], a[-1])

#after initializing as array and slicing
b=np.array([6,7,8])
print(b[0:2], b[-1])

#multi dimensional array
c=np.array([[6,7,8],[1,2,3],[9,3,2]])
print(c[1,2]) #This fetches the 2nd row 3rd value
print(c[0:2,2]) #This fetches the 1st 2 rows 3rd value
print(c[-1]) #this fetches the last row
print(c[-1,0:2]) #this will print 1st 2 columns of last row
print(c[:,1:3]) #this will print last 2 columns

print(c.flat)
for cell in c.flat:
    print(cell)

#Stacking arrays
d=np.arange(6).reshape(3,2)
print(d)
e=np.arange(6,12).reshape(3,2)
print(e)

print(np.vstack((d,e)))
print(np.hstack((d,e)))

#array split
f = np.arange(30).reshape(2,15)
print(f)
print(np.hsplit(f,3))
print(np.vsplit(f,2))

g = np.arange(12).reshape(3,4)
h=g>4 #generates boolean array
print(g)
print(h)
#conditional element extraction
print(g[h])

g[h]=-1 #all qualifying elements will be turned -1
print(g)