import pandas as pd
import numpy as np
import random
from matplotlib import legend, pyplot as plt

def calc_distance(X1, X2):
  return(sum((X1 - X2)**2))**0.5

def findClosestCentroids(ic, X):
  assigned_centroid = []
  for i in X:
    distance=[]
    for j in ic:
      distance.append(calc_distance(i, j))
    assigned_centroid.append(np.argmin(distance))
  return assigned_centroid

def calc_centroids(clusters, X):
  new_centroids = []
  new_df = pd.concat([pd.DataFrame(X), pd.DataFrame(clusters, columns=['cluster'])],axis=1)
  for c in set(new_df['cluster']):
    current_cluster = new_df[new_df['cluster'] == c][new_df.columns[:-1]]
    cluster_mean = current_cluster.mean(axis=0)
    new_centroids.append(cluster_mean)
  return new_centroids

data_file_select = int(input("1. Iris\n2. Glass\nINPUT: "))
k_val = int(input("Enter value for 'K' (int)\nINPUT: "))
if data_file_select == 1:
  iris = pd.read_csv('data/iris/iris.data')
  iris.head()
  X = np.array(iris)
  centroids = []
  init_centroids = random.sample(range(0, len(iris)), k_val)
  for i in init_centroids:
    centroids.append(iris.loc[i])
  centroids = np.array(centroids)
  get_centroids = findClosestCentroids(centroids, X)
  for i in range(10):
    get_centroids = findClosestCentroids(centroids, X)
    centroids = calc_centroids(get_centroids, X)
elif data_file_select == 2:
  glass = pd.read_csv('data/glass/glass.data')
  glass.head()
  X = np.array(glass)
  centroids = []
  init_centroids = random.sample(range(0, len(glass)), k_val)
  for i in init_centroids:
    centroids.append(glass.loc[i])
  centroids = np.array(centroids)
  get_centroids = findClosestCentroids(centroids, X)
  for i in range(10):
    get_centroids = findClosestCentroids(centroids, X)
    centroids = calc_centroids(get_centroids, X)
else:
  exit()

plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], color='red')
plt.scatter(X[:, 0], X[:, 1], alpha=0.5)
plt.show()
