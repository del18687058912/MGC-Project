import numpy as np
import kl_divergence as kl
import track_features as tf
from sklearn import neighbors

def knn_classification():
	training_samples_count = 70
	testing_samples_count = 30
	print "Read training data"
	training_array = []
	training_classes = []

	training_set_features = tf.get_features("../../music/training", training_samples_count, "rock" , "pop", "class", "jazz")

	# get features count
	n_features = len(training_set_features[0][0])

	# convert each cortege to array
	for track_features in training_set_features:
		training_array[len(training_array):] = [tf.cortege_to_list(track_features, n_features)]
		training_classes[len(training_classes):] = [tf.get_genre_ID(str(track_features[2]))]

	knn_classifier = neighbors.KNeighborsClassifier( weights='uniform', algorithm='ball_tree', 
										metric=kl.calculate_KL_divergence, metric_params={"n_features": n_features})
	knn_classifier.fit(training_array,training_classes)
	print "Read testing data"
	testing_set_features = tf.get_features("../../music/testing", testing_samples_count, "rock", "pop", "class", "jazz")
	testing_array = []
	expected_genres = []

	# convert each cortege to array
	for track_features in testing_set_features:
		testing_array[len(testing_array):] = [tf.cortege_to_list(track_features, n_features)]
		expected_genres[len(expected_genres):] = [track_features[2]]

	#print testing_array
	result_of_classification = knn_classifier.predict(testing_array)

	result = []
	for result_class in result_of_classification:
		result[len(result):] = [tf.get_genre_name(result_class)]
	print "Expected: ", expected_genres
	print "Result: ", result
	
	rock_count = 0
	pop_count = 0
	class_count = 0
	jazz_count = 0
	for i in range(len(expected_genres)):
		if (expected_genres[i] == result[i]):
			if expected_genres[i] == "rock":
				rock_count+=1
			elif expected_genres[i] == "pop":
				pop_count+=1
			elif expected_genres[i] == "class":
				class_count+=1
			elif expected_genres[i] =="jazz":
				jazz_count+=1

	rock_probability = float(rock_count) / int(testing_samples_count)
	pop_probability = float(pop_count) / int(testing_samples_count)
	class_probabolity = float(class_count) / int(testing_samples_count)
	jazz_probability = float(jazz_count) / int(testing_samples_count)

	print "rock:  ", rock_count, rock_probability
	print "pop:   ", pop_count, pop_probability
	print "class: ", class_count, class_probabolity
	print "jazz:  ", jazz_count, jazz_probability 

knn_classification()