from numpy import*
a=random.randint(0,10,(3,3))
b=count_nonzero(a)
c=count_nonzero(a>5)
cc=count_nonzero(a>5,axis=1)#تبحث في القيمة الكبرى لكل سطر على حدى

print(a)
print(b)
print(c)
print(cc)
print(any(a>5))# هل هناك قيمة اكبر من 5
print(any(a>5, axis=1))# 
print(all(a>1,axis=1))

print("@"*50)
a=random.randint(0,20,size=9).reshape(3,3)
b=a>10
c=a<15
d=a[b]#print the numbers of values true 
e=a[c]
print(a)
print(b)
print(c)
print(d)
print(e)

print("@"*50)
a=arange(0, 9).reshape(3,3)
b=arange(0, 9).reshape(3,3)
c=2*b
d=isclose(a, b,rtol=0.1)
e=isclose(a, c,rtol=0.5)#rtol  هل المصفوفتين متقاربتين بمقدار النصف
print(a)
print(b)
print(c)
print(d)
print(e)

print("@"*50)
a=arange(1, 6)
c=random.randint(5,25,size=5)
b=empty(5)
multiply(a,c,out=b)
print(a)
print(b)





