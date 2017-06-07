import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg
from numpy import matrix

A = np.matrix([[1,8],
			[1,2],
			[1,11],
			[1,6],
			[1,5],
			[1,4],
			[1,12],
			[1,9],
			[1,6],
			[1,1]])

R = np.matrix([3,10,3,6,8,12,1,4,9,14])

print("\nMATRIZ A: ")
print(A)
AT = A.T

print("\nMATRIZ R:")
print(R)

print("\nMATRIZ AT: ")
print(AT)

ATA = np.dot(AT, A)
print("\nMATRIZ ATA: ")
print(ATA)

b = np.dot(AT,R.T)
print("\nMATRIZ b: ")
print(b)

x = np.linalg.inv(ATA).dot(b)
print("\nMATRIZ x: ")
print(x)

plt.plot([-x[0]/x[1],0],[0,x[0]])

for i in range(0,10):
	plt.plot(A[i,1],R[0,i], 'ro')

plt.axis([0, 15, 0, 15])
plt.show()



