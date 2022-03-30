import numpy as np
from pandas import *
#كثيرة الحدود
p=np.polynomial.Polynomial
X=np.array([20,40,60,80,100,120,140,160,180])
Y=np.array([10,9,8,7,6,5,4,3,1])
points,stats=p.fit(X,Y,1,full=False)

print(points,stats)

points.plot(kind='line')