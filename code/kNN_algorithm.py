import numpy as np
import kl_divergence as kl
import track_features as tf
import routine as rt
from sklearn import neighbors

def knn_classification(genres):
	training_samples_count = 70
	testing_samples_count = 30
	print "Read training data"
	training_array = []
	training_classes = []

	training_set_features = tf.read_features_from_files("../../music/training", genres)

	# get features count
	n_features = len(training_set_features[0][0])

	# convert each cortege to array
	for track_features in training_set_features:
		training_array[len(training_array):] = [tf.cortege_to_list(track_features)]
		training_classes[len(training_classes):] = [tf.get_genre_ID(str(track_features[2]))]


	print "Read testing data"
	testing_set_features = tf.read_features_from_files("../../music/testing", genres)
	testing_array = []
	expected_genres = []

	# convert each cortege to array
	for track_features in testing_set_features:
		testing_array[len(testing_array):] = [tf.cortege_to_list(track_features)]
		expected_genres[len(expected_genres):] = [tf.get_genre_ID(str(track_features[2]))]

	for weight in ['distance', 'uniform']: 
		for n_neighbors in range(3,6):
			knn_classifier = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, weights=weight, algorithm='ball_tree',
											metric=kl.calculate_KL_divergence, metric_params={"n_features": n_features})
			knn_classifier.fit(training_array,training_classes)
			result_of_classification = knn_classifier.predict(testing_array)
			result = []
			params_string = "weight: " + str(weight) + " n_neighbors: " + str(n_neighbors)
			rt.print_accuracy(expected_genres, result_of_classification, genres, params_string)
