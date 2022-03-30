from numpy import *
x=array('2022-03-07',dtype=datetime64)
z=array('2022-07-01',dtype=datetime64)
print(x)
y=z-x
print(y)

print("@"*30)
a=fromfunction(lambda i:i**3,(10,))

print(a)

print("#"*50)

a=fromfunction(lambda i,j:4*i+j,(4,7))

print(a)


def p(i,j):
    i=i**j
    return i


x=fromfunction(p,(4,5),dtype=int)
print(x)
