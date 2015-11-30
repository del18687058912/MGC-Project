import numpy as np
import math
import track_features

def calculate_KL_divergence_unsym(features_1, features_2):

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

def calculate_KL_divergence(features_1,features_2):
	return calculate_KL_divergence_unsym(features_1,features_2) + calculate_KL_divergence_unsym(features_2,features_1)