import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

img = plt.imread('image.jpg')
# plt.imshow(img)
# plt.show()
# plt.axis('off');

# cluster number
k = 3

def image_cluster(img, k):
    img_flat = img.reshape(img.shape[0]*img.shape[1],3)
    kmeans = KMeans(n_clusters=k, random_state=0).fit(img_flat)
    img_flat2 = img_flat.copy()

    # loops for each cluster center
    for i in np.unique(kmeans.labels_):
        img_flat2[kmeans.labels_==i,:] = kmeans.cluster_centers_[i]
        print(i)
        
    img2 = img_flat2.reshape(img.shape)
    return img2, kmeans.inertia_

# show the image with k clusters
img2, inertia = image_cluster(img, k)

print("\nInertia: ", inertia)

plt.imshow(img2)
plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(1, 2, 1)
# imgplot = plt.imshow(img)
# ax.set_title('Before')

# ax = fig.add_subplot(1, 2, 2)
# imgplot = plt.imshow(img2)
# imgplot.set_clim(0.0, 0.7)
# ax.set_title('After')

# plt.show()

