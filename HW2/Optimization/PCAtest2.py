from sklearn import datasets
from sklearn import decomposition
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from mpl_toolkits.mplot3d import Axes3D

#matplotlib notebook

mnist = datasets.load_digits()
X = np.linspace(-10, 10, 1000)[:, np.newaxis]
y = np.sin(5*math.pi*X)/(5*math.pi*X)
pca = decomposition.PCA(n_components=3)
new_X = pca.fit_transform(X)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(new_X[:, 0], new_X[:, 1], new_X[:, 2], c=y)
plt.show()