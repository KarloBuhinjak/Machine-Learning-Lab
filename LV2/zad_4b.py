
import matplotlib.pyplot as plt
import numpy as np
import skimage.io
img = skimage.io.imread('tiger.png', as_gray=True)
plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

rows,cols= img.shape

empty_img = np.zeros((cols,rows))

for i in range(rows):
        empty_img[:,-i]=img[i,:]


plt.figure(2)
plt.imshow(empty_img, cmap='gray', vmin=0, vmax=255)

plt.show()