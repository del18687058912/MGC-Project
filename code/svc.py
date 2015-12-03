from sklearn import datasets
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import SVC
import numpy as np
import track_features as tf

def print_accuracy(expected_class, actual_class, genres):
	genres_correct = [0 for i in range(len(genres))]
	genres_total = [expected_class.count(tf.get_genre_ID(genres[i])) for i in range(len(genres))]

	genres_correct_total = 0
	for i in range(len(expected_class)):
		if (expected_class[i] == actual_class[i]):
			pos = genres.index(tf.get_genre_name(expected_class[i]))
			genres_correct[pos] += 1
			genres_correct_total += 1

	print "Accuracy:"
	for i in range(len(genres)):
		print genres[i] + ":", genres_correct[i], float(genres_correct[i]) / float(genres_total[i])
	print "averege:" , float(genres_correct_total) / float(len(actual_class))

def svm_classification():
	training_set_features = tf.read_features_from_files("../../music/training", "rock", "pop", "class", "jazz")
	testing_set_features = tf.read_features_from_files("../../music/testing", "rock", "pop", "class", "jazz")

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

	print_accuracy(list(testing_class), list(result_class), ["rock", "pop", "class", "jazz"])
	