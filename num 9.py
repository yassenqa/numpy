from numpy import*
fname= 'C:/Users/SEB/Desktop/course 2/numfile.txt'
d=dtype([('gender','|S1'),('height','f8')])
a=loadtxt(fname,dtype=d,skiprows=9,usecols=(1,3))
print(a)





