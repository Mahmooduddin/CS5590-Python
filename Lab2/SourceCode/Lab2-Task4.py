#import NumPy
import numpy as np
# create random vector of size 15
x = np.random.random(15)
#print original vector
print("\nOriginal vector:\n")
print(x)
#find max value in original vector
max1 = np.amax(x)
#print max value of original vector
print("\nMaximum value in original vector is:",max1)
#repalce max value by 100
x[x.argmax()] = 100
#print vector
print("\nMaximum value replaced by 100:\n")
print(x)