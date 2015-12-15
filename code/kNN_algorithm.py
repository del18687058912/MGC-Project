import numpy as np
import kl_divergence as kl
import track_features as tf
import routine as rt
from sklearn import neighbors

''' K-Nearest Neighbors classification algorithm

Parameters
-----------

	genres : array of shape [n_genres]
		List of genres to use.

	features_type : {'fbank', 'mfcc'}, optional (default='mfcc')
		Features used to classify genres:

		- 'fbank': Filter bank features (n_features=26)
		- 'mfcc': Mel Frequency Cepstral Coefficient (n_features=13)

	weight : {'distance', 'uniform'}, optional (default='distance')
		Weight function used in prediction.

        - 'uniform' : uniform weights.  All points in each neighborhood
          are weighted equally.
        - 'distance' : weight points by the inverse of their distance.
          in this case, closer neighbors of a query point will have a
          greater influence than neighbors which are further away.

    n_neighbors_min : int, optional (default=3)
    	Minimum number of neighbors for which classification will be run

    n_neighbors_max : in, optional (default=5)
    	Maximum number of neighbors for which classification will be run
'''
def knn_classification(genres, features_type='mfcc', weight='distance', n_neighbors_min=3, n_neighbors_max=5):
	training_array = []
	training_classes = []

	training_set_features = tf.read_features_from_files("../../music/training", genres, features_type)

	n_features = len(training_set_features[0][0])

	# convert each cortege to array
	for track_features in training_set_features:
		training_array[len(training_array):] = [tf.cortege_to_list(track_features)]
		training_classes[len(training_classes):] = [tf.get_genre_ID(str(track_features[2]))]

	testing_set_features = tf.read_features_from_files("../../music/testing", genres, features_type)
	testing_array = []
	expected_genres = []

	# convert each cortege to array
	for track_features in testing_set_features:
		testing_array[len(testing_array):] = [tf.cortege_to_list(track_features)]
		expected_genres[len(expected_genres):] = [tf.get_genre_ID(str(track_features[2]))]

	for n_neighbors in range(n_neighbors_min, n_neighbors_max+1):
		knn_classifier = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, weights=weight, algorithm='ball_tree',
											metric=kl.calculate_KL_divergence, metric_params={"n_features": n_features})
		knn_classifier.fit(training_array,training_classes)
		result_of_classification = knn_classifier.predict(testing_array)
		result = []

		params_string = "weight: " + str(weight) + " n_neighbors: " + str(n_neighbors)
		rt.print_accuracy(expected_genres, result_of_classification, genres, features_type, "knn", params_string)
		rt.write_accuracy_to_file("../../music/", expected_genres, result_of_classification, genres, features_type, "knn", params_string)
