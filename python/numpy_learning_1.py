import numpy as np

#define array
a=np.array([5,6,9])
print(a)

#array properties
b = np.array([[1,2],[3,4],[5,6]])
print(b)
print("ndim:", b.ndim)
print("itemsize:", b.itemsize)
print("datatype:", b.dtype)

c = np.array([[1,2],[3,4],[5,6]], dtype=float)
print("itemsize:", c.itemsize)
print(c)
print("size:",c.size)
print("shape:",c.shape)

d = np.array([[1,2],[3,4],[5,6]], dtype=complex)
print(d)

#zeros
e = np.zeros((3,4))
print(e)

#ones
f = np.ones((3,4))
print(f)

#range
g = range(3)
print(g[0],g[1],g[2])

#arange
h = np.arange(1,5)
print(h)

#arange with step
i = np.arange(1,5,2)
print(i)

#linspace
j=np.linspace(1,5,10)
print(j)

#reshape
k = np.array([[1,2],[3,4],[5,6]])
print(k)
print(k.shape)
print(k.reshape(2,3))
#print(k.reshape(10,10))

#ravel - to flatten the array
print(k.ravel())

#min and max
print(k.min(), k.max(), k.sum())

#axis axis 0 - columns and axis 1 - rows
print(k.sum(axis=0))
print(k.sum(axis=1))

#square root
print(np.sqrt(k))

#standard deviation
print(np.std(k))

l = np.array([[1,2],[3,4]])
m = np.array([[5,6],[7,8]])
print(l+m)
print(l*m)
print(l/m)

#matrix product
print(l.dot(m))