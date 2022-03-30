import numpy as py
print (py.__version__)
d=py.array([[[5,6],[7,9]],[[1,3],[4,8]],[[1,2],[5,8]]])
print(d[2,1,1])

m=py.array([1,2,3],ndmin=3)
print(m)

l=100
my=py.arange(l)
my2=py.arange(l)
print(my+my2)


v=py.array(["a","b","y"," "])
print(v)
v=v.astype('bool')
print(v)
























