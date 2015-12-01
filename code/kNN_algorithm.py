import numpy as np
from kl_divergence import calculate_KL_divergence
from sklearn import neighbors

def knn_classification():
	a = [0,1,3]
	b = [[10,0,0],[0,1,0],[0,0,1]]
	b1 = [[10,1,0],[0,1,0],[0,0,1]]
	c = [7,8,9]
	d = [[10,2,4],[4,8,6],[12,.8,16]]
	e = [0,1,3]
	g = [[50,5,5],[15,.1,5],[7,.5,.13]]

	f1 = (a, b)
	f2 = (c, d)
	f3 = (a, d)
	f4 = (c, b)
	f5 = (e, b)
	f6 = (e, g)

	a1 = np.concatenate([a,np.array(b).ravel()])
	a2 = np.concatenate([c,np.array(d).ravel()])
	a3 = np.concatenate([a,np.array(d).ravel()])
	a4 = np.concatenate([c,np.array(g).ravel()])
	a5 = np.concatenate([e,np.array(b1).ravel()])
	a6 = np.concatenate([e,np.array(b1).ravel()])

	print(a1, a2, a3, a4, a5)

	size = len(a)
	X = np.array([a1, a2, a3, a4, a5])
	y = [0, 1, 2, 3, 4]
	Z = np.array([a6])

	print(X)
	print(y)

	nbrs = neighbors.KNeighborsClassifier(n_neighbors=2,  weights='distance', 
										metric=calculate_KL_divergence, metric_params={"n_features": size})
	nbrs.fit(X,y)
	Z1 = nbrs.predict(Z)
	print(Z1)

knn_classification()

