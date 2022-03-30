from numpy import * 
a=random.rand(2,3,3)
print(a)
print("#"*50)
y=array([[1,2,3,4,5,6,7,8,9],[5,4,7,8,9,6,6,3,1]])

#e=random.choice(y)
#rint(e)
random.shuffle(y[1])
random.shuffle(y[0])
print(y)

print("#"*50)
a=zeros(5)
b=ones((2,3,4))
print(a)
print(b)

print("#"*50)
a=eye(5)
print(a)

print("#"*50)
a=full((3,2), 40)
print(a)

print("#"*50)
a=arange(0, 20)
random.shuffle(a)
r=reshape(a,(4,5))
print(r)

print("#"*50)
# طرح الرقمين   على عدد الخطوات
a=linspace(0, 10)#تلقائي 50 رقم
print(a)
a=linspace(10, 100,5)#تلقائي 50 رقم
print(a)

print("#"*50)
z=array([1,2,3,4,5,6,7])

a=diag(z)
b=diag(z,k=2)

print(a)
print(b)
















