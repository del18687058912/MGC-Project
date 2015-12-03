import numpy as np
import track_features as tf
import math
from sklearn.neighbors.dist_metrics import DistanceMetric
from sklearn.metrics.pairwise import euclidean_distances

def _calculate_KL_divergence_unsym(features_1, features_2):
	mean_1 = features_1[0]
	mean_2 = features_2[0]

	covariance_1 = np.asmatrix(features_1[1])
	covariance_2 = np.asmatrix(features_2[1])

	inverse_2 = np.linalg.inv(covariance_2)
	mean_diff = np.subtract(mean_2, mean_1)

	# Calculate terms of KL_divergence
	trace_of_mult = np.trace(np.dot(inverse_2, covariance_1))
	mult = np.dot(mean_diff, np.array(np.dot(covariance_2, mean_diff)).ravel())
	dimension = len(mean_1)
	log_of_det_div = math.log(np.linalg.det(covariance_2) / np.linalg.det(covariance_1))

	KL_divergence = 0.5*(trace_of_mult + mult - dimension + log_of_det_div)
	return KL_divergence;

def calculate_KL_divergence(features_1,features_2, **kwargs):
	n_features = kwargs["n_features"]
	if (len(features_1) < n_features*(n_features+1)):
		return np.linalg.norm(features_1 - features_2)
	f1 = tf.list_to_cortege(features_1,n_features)
	f2 = tf.list_to_cortege(features_2,n_features)
	return _calculate_KL_divergence_unsym(f1,f2) + _calculate_KL_divergence_unsym(f2,f1)
