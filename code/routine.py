import track_features as tf

def print_accuracy(expected_class, actual_class, genres, features_type, *extra_string):
	genres_correct = [0 for i in range(len(genres))]
	genres_total = [expected_class.count(tf.get_genre_ID(genres[i])) for i in range(len(genres))]

	genres_correct_total = 0
	for i in range(len(expected_class)):
		if (expected_class[i] == actual_class[i]):
			pos = genres.index(tf.get_genre_name(expected_class[i]))
			genres_correct[pos] += 1
			genres_correct_total += 1

	print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
	print features_type
	print genres
	for string in extra_string:
		if len(string) != 0:
			print string
	print "Accuracy:"
	for i in range(len(genres)):
		print genres[i] + ":", genres_correct[i], float(genres_correct[i]) / float(genres_total[i])
	print "average:" , float(genres_correct_total) / float(len(actual_class))
	print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"