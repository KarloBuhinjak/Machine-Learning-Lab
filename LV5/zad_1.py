from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def generate_data(n_samples, flagc):
    
    if flagc == 1:
        random_state = 365
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        
    elif flagc == 2:
        random_state = 148
        X,y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)
        
    elif flagc == 3:
        random_state = 148
        X, y = datasets.make_blobs(n_samples=n_samples,
                                    centers=4,
                                    cluster_std=[1.0, 2.5, 0.5, 3.0],
                                    random_state=random_state)

    elif flagc == 4:
        X, y = datasets.make_circles(n_samples=n_samples, factor=.5, noise=.05)
        
    elif flagc == 5:
        X, y = datasets.make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

X=generate_data(500,1)
plt.figure(1)
plt.scatter(X[:,0],X[:,1])
plt.title("Podaci")
plt.xlabel("x_1")
plt.ylabel("x_2")
plt.show()


model=KMeans(n_clusters=3)
model.fit(X)
b=model.predict(X)


plt.figure(2)
plt.title("Rezultat ")
plt.xlabel("x_1")
plt.ylabel("x_2")
plt.scatter(X[:,0],X[:,1],c=b)
plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,1], c='b',marker='x')
plt.show()


inertia=[]

for i in range(1,20):
    model=KMeans(n_clusters=i)
    model.fit(X)

    inertia.append(model.inertia_)

print(inertia)

plt.figure(3)
plt.title("Inercija za razlicit broj klastera")
plt.plot(inertia,'b-o')
plt.xlabel('broj klastera')
plt.ylabel('inercija')
plt.show()