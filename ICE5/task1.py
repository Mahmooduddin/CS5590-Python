import numpy as np
import matplotlib.pyplot as plt

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

mean1=np.mean(a)
mean2=np.mean(b)

print(mean1)
print(mean2)

AB= np.multiply((a-mean1),(b-mean2))
print(AB)
C= np.multiply((a-mean1),(a-mean1))
print(C)
z3=np.sum(AB)
print(AB)
z4=np.sum(C)
print(C)
B1= np.divide(z3,z4)
print("B1 is", B1)
B1x=np.multiply(B1,mean1)
B0=np.subtract(mean2,B1x)
print("B0 is", B0)
X=np.multiply(B1,a)
Y=B0+X
plt.plot(a,Y)
plt.scatter(a,b)
plt.show()