from numpy import*
a=arange(1, 16)
b=add.reduce(a)#بيجمع اعداد المصفوفة مع بعضعها
print(b)
c=multiply.reduce(a)
print(c)

print("!"*50)
a=arange(1, 11)
b= multiply.outer(a,a)#نأخذ العدد الاول ونضربه بكل الارقام فيصبح عندنا صف والرقم الثاني نضربه بجميع الارقام فينتج الصف الثاني وهكذا
print(a)
print(b)

print("!"*50)
a=arange(1, 11)
b=add.accumulate(a)#جمع العنصر مع جميع العناصر الي قبله #
print(a)
print(b)

print("1"*50)
a=arange(1, 11)

c=multiply.accumulate(a)#كل عنصر نضربه بالعناصر الي قبله
print(a)
print(c)

print("!"*50)
a=arange(12)
print(len(a))
b=reshape(a, (3,4))
print(len(b))#عدد الاسطر
print(size(b))#كل العناصر
print(shape(b))
print(b.ndim)# البعد
print(b.dtype)#نوع البيانات
print("!"*50)




