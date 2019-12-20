import matplotlib.cm as cm
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('mydata_short.csv', delimiter=',', usecols=(0, 1, 2, 3, 4, 5), skip_header=(1))
col_1 = data[:, 1]
col_2 = data[:, -1]
df = pd.DataFrame({
    'x': col_1,
    'y': col_2
})
# df = pd.DataFrame({
#     'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
#     'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
# })


kmeans = KMeans(n_clusters=5)
kmeans.fit(df)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(15, 15))

# colmap = {1: 'r', 2: 'g', 3: 'b'}
# colors = list(map(lambda x: colmap[x+1], labels))

x = np.arange(len(df['x']))
ys = [i+x+(i*x)**2 for i in range(len(df['x']))]
colors = cm.rainbow(np.linspace(0, 1, len(ys)))

plt.scatter(df['x'], df['y'], color=colors, alpha=0.5, edgecolor='k')
for idx, centroid in enumerate(centroids):
    plt.scatter(*centroid, color=colors[idx+1])
plt.xlim(0, 3)
plt.ylim(0, 3)
plt.show()
