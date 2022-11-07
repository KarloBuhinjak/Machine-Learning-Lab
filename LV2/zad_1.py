import matplotlib.pyplot as plt

x = [1, 2, 3, 3, 1]
y = [1, 2, 2, 1, 1]
plt.plot(x,y,"r-")
plt.scatter(x,y,color="red")
plt.title("Primjer")

plt.xlim([0, 4])
plt.ylim([0, 4])


plt.show()
