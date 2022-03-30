from numpy import*

# add
a=random.randint(2,20,size=9).reshape(3,3)
b=random.randint(2,20,size=9).reshape(3,3)
z=a+b
d=a-b
print(a,"\n",b,"\n","\n",z,"\n",d)

#mult
print("!"*50)
#first
a=random.randint(2,20,size=9).reshape(3,3)
b=random.randint(2,20,size=9).reshape(3,3)
z=a*b
d=a/b
print(a)
print(b)
print(z)
print(d)
#scand
print("2"*50)
a=random.randint(2,20,size=9).reshape(3,3)
b=random.randint(2,20,size=9).reshape(3,3)
z=a*3
y=sin(a)
d=a/5

print(a)
print(b)
print(y)
print(z)
print(d)
#third
print("2"*50)
a=random.randint(2,20,size=4).reshape(2,2)
b=random.randint(2,20,size=8).reshape(2,4)
c=dot(a, b)
print(a)
print(b)
print(c)

print("!"*50)
a=random.randint(5,20,size=9).reshape(3,3)
b= sum (a)
c=a.sum()
d=a.sum(axis=1)
e=a.sum(axis=0)
print(a)
print(b)
print(c)
print(d)
print(e)

print("!"*50)
a=random.randint(5,20,size=9).reshape(3,3)
b=a.mean()
c=a.std()
d=a.var()#الانحراف
print(a)
print(b)
print(c)
print(d)
print("!"*50)
a=random.randint(5,20,size=9).reshape(3,3)
s=sort(a,axis=1)
ss=sort(a,axis=0)
sss=sort(a)
b=linalg.inv(a)#معكوس ايع
c=dot(a,b)
print(a)
print(s)
print(ss)
print(sss)
print(b)
print(c)




