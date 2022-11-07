
import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
array = np.array(data)
weight = np.array(array[:,5])
mpg = np.array(array[:,0])
hp = np.array(array[:,3])
plt.scatter(mpg, hp, s=weight*10)
plt.xlabel("mpg")
plt.xlabel("hp")

print("Min value of mpg: ", np.min(mpg))
print("Max value of mpg: ", np.max(mpg))
print("Mean value of mpg: ", np.mean(mpg))

print(data)

plt.show()