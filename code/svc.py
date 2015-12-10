from sklearn import datasets
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import SVC
import numpy as np
import track_features as tf
import routine as rt

def svm_classification(genres, features_type):
	training_set_features = tf.read_features_from_files("../../music/training", genres, features_type)
	testing_set_features = tf.read_features_from_files("../../music/testing", genres, features_type)

	X = []
	y = []
	for feature in training_set_features:
		(mean, cov_mat, genre_name) = feature
		X.append(mean.tolist())
		y.append(tf.get_genre_ID(genre_name))

	training_data = np.array(X)
	training_class = np.array(y)

	X = []
	y = []
	for feature in testing_set_features:
		(mean, cov_mat, genre_name) = feature
		X.append(mean.tolist())
		y.append(tf.get_genre_ID(genre_name))

	testing_data = np.array(X)
	testing_class = np.array(y)


	clf = OneVsOneClassifier(SVC(kernel='linear'))
	result_class = np.array(clf.fit(training_data, training_class).predict(testing_data))

	rt.print_accuracy(list(testing_class), list(result_class), genres, features_type, "svm")
	rt.write_accuracy_to_file("../../music/", list(testing_class), list(result_class), genres, features_type, "svm")
