from numpy import *
a=[2,3,4,5,6,8]
b=array(a)
print(a)
print(b)
aa=[[1,2,3],[3,5,6],[5,4,3]]
bb=array(aa)
print(aa)
print(bb)
# new 
print("!"*50)
aaa=array([range(i,i+3)for i in [2,8,6]])
print(aaa)
print("!"*50)
m=empty((3,2))
print(m)
print("!"*50)

z=random.uniform(1,10)
zz=random.uniform(1,10,5)

print(z)

print(zz)
print("!"*50)

# array
q=random.random((2,3))
print(q+10)

print("!"*50)
w=random.normal(0,6,6)#start , range , كم قيمة 
print(w)
print("!"*50)
e=random.randint(145,182,size=7)
ee=random.randint(0,10,(3,5))
eee=random.randint(0,10, size=(3,4,8))
print(e)
print(ee)
print(eee)

print("!"*50)

r=random.randint(1,25,12)
rr=reshape(r,(3,4))
print(r)
print(rr)








