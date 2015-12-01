import numpy as np
from kl_divergence import calculate_KL_divergence
import track_features as tf
from sklearn import neighbors

def knn_classification():
	print "Read training data"
	training_set_features_array = []
	training_set_classes = []
	training_set_features = tf.get_features("../../music/training", "rock" , "pop", "class", "jazz")

	# convert each cortege to array
	for track_features in training_set_features:
		features_array = np.concatenate([track_features[0], np.array(track_features[1]).ravel()])
		training_set_features_array[len(training_set_features_array):] = [features_array]
		training_set_classes[len(training_set_classes):] = [tf.get_genre_ID(str(track_features[2]))]
	
	# get features count
	n_features = len(training_set_features[0][0])

	print "Read testing data"
	testing_set_features = tf.get_features("../../music/testing", "jazz")
	testing_set_features_array = []
	expected_genres = []

	# convert each cortege to array
	for track_features in testing_set_features:
		features_array = np.concatenate([track_features[0], np.array(track_features[1]).ravel()])
		testing_set_features_array[len(testing_set_features_array):] = [features_array]
		expected_genres[len(expected_genres):] = [tf.get_genre_ID(str(track_features[2]))]

	testing_data = np.array(testing_set_features_array)

	knn_classifier = neighbors.KNeighborsClassifier(n_neighbors=4,  weights='distance', 
										metric=calculate_KL_divergence, metric_params={"n_features": n_features})
	knn_classifier.fit(training_set_features_array,training_set_classes)
	result_of_classification = knn_classifier.predict(testing_data)

	print "Expected: ", tf.get_genre_name(expected_genres[0])
	print "Result: ", tf.get_genre_name(result_of_classification[0])

knn_classification()

