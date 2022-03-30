from numpy import*
a=matrix('{} {} ; {} {}'.format(1,2,3,4))
pb=matrix('{} {} {};{} {} {}'.format(1,2,3,4,5,6))
print(a)
print(b)

print("!"*50)
a=arange(0, 9)
b=reshape(a, (3,3))
d=trace(b)#جمع عناصر القطر الرئيسي
print(b)
print(d)

print("!"*50)
a=arange(5,14)
b=a.reshape(3,3)
c=linalg.det(b)# محدود مصفوفة
print(b)
#cc=linalg.eig(b)#unknwon
print(c)
#print(cc)

print("!"*50)
a=arange(0, 36)
b=reshape(a, (6,6))
print(b)
z=b[2]#صف
q=b[2,[2]]#listعنصر
c=b[2,2]#عنصر
print(z)
print(c)
print(q)
aa=b[3,2:9:2]
print(aa)

m=b[::-1,::-1]#عكس المصفوفة
print(m)
mm=b[:2:-1,:3:-1]
print(mm)
print("!"*50)










