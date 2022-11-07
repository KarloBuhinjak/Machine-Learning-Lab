
import matplotlib.pyplot as plt
import numpy as np
import skimage.io
img = skimage.io.imread('tiger.png', as_gray=True)
plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

rows,cols= img.shape

empty_img = np.zeros((rows,cols))


for j in range(cols):
        empty_img[:,j]=img[:,cols-1-j]

plt.figure(2)
plt.imshow(empty_img, cmap='gray', vmin=0, vmax=255)
plt.show()