from numpy import*
a= arange(16).reshape(4,4)
b= a[:,1:3]#a تعدل لانها جزء من 
c= a[:,1:3].copy()#لا تعدل لانها نسخة
print(b)
print(c)
a[:,:]=5
print(a)
print(b)
print(c)

print("!"*50)
x=[1,2,3,4,5,6,7,8]
z,c,v=split(x, (4,6))
print(z,c,v)

print("!"*50)
a= arange(16).reshape(4,4)
b= arange(12).reshape(3,4)
c=vstack((a,b))#يجب ان يكون العواميد متاوية بالعدد
print(a)
print(b)
print(c )

print("!14"*50)
a= arange(16).reshape(4,4)
b= arange(12).reshape(4,3)
c=hstack((a,b))#يجب ان يكون الصفوف متاوية بالعدد
print(a)
print(b)
print(c)

print("!"*50)
a=random.randint(5,20,size=9).reshape(3,3)
d=argmax(a)#عدد القيم التي اكبر من المتوسط الحسابي
c=argmin(a)#عدد القيم التي اصغر من المتوسط الحسابي
dd=var(a)
cc=cov(a)
print(a)
print(d)
print(c)
print(dd,cc)

