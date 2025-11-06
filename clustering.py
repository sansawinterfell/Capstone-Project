import pandas as pd 
import numpy as np 
import pickle 
from sklearn.cluster import KMeans


data=pd.read_csv
X = np.array(data)

number_of_clusters=4


kmean = KMeans (
    n_clusters=4,
	init='k-means++',
	max_iter=300,
	n_init=10,
	random_state=19890528,
	precompute_distances=True)

kfit = kmeans.fit(X)

freeze_centroids = kmeans.cluster_centers_
print(freeze_centroids)
print(freeze_centroids.shape)