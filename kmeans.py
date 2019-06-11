from copy import deepcopy
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt

center_1 = np.array([1,1])
center_2 = np.array([5,5])
center_3 = np.array([8,1])

data_1 = np.random.randn(200, 2) + center_1
data_2 = np.random.randn(200,2) + center_2
data_3 = np.random.randn(200,2) + center_3

data = np.concatenate((data_1, data_2, data_3), axis = 0)

plt.scatter(data[:,0], data[:,1], s=7)

k = 3
n = data.shape[0]
c = data.shape[1]

mean = np.mean(data, axis = 0)
std = np.std(data, axis = 0)
centers = np.random.randn(k,c)*std + mean

plt.scatter(data[:,0], data[:,1], s=7)
plt.scatter(centers[:,0], centers[:,1], marker='*', c='g', s=150)

centers_old = np.zeros(centers.shape) # to store old centers
centers_new = deepcopy(centers) # Store new centers

data.shape
clusters = np.zeros(n)
distances = np.zeros((n,k))

error = np.linalg.norm(centers_new - centers_old)

while error != 0:
    for i in range(k):
        distances[:,i] = np.linalg.norm(data - centers[i], axis=1)
        clusters = np.argmin(distances, axis = 1)
    
    centers_old = deepcopy(centers_new)
        for i in range(k):
        centers_new[i] = np.mean(data[clusters == i], axis=0)
    error = np.linalg.norm(centers_new - centers_old)
centers_new 

plt.scatter(data[:,0], data[:,1], s=7)
plt.scatter(centers_new[:,0], centers_new[:,1], marker='*', c='g', s=150)

