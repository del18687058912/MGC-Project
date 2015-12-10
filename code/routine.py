import os
import track_features as tf

def get_accuracy(expected_class, actual_class, genres, features_type, *extra_strings):
	genres_correct = [0 for i in range(len(genres))]
	genres_total = [expected_class.count(tf.get_genre_ID(genres[i])) for i in range(len(genres))]

	genres_correct_total = 0
	for i in range(len(expected_class)):
		if (expected_class[i] == actual_class[i]):
			pos = genres.index(tf.get_genre_name(expected_class[i]))
			genres_correct[pos] += 1
			genres_correct_total += 1
	extra_string = ""
	for string in extra_strings:
		if len(string) != 0:
			extra_string += str(string) + "\n"
	result = ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n" + \
	str(features_type) + "\n" + \
	str(genres) + "\n" + \
	str(extra_string) + \
	"Accuracy: \n"
	for i in range(len(genres)):
		result += str(genres[i]) + ": " + str(genres_correct[i]) + " " + str(float(genres_correct[i]) / float(genres_total[i])) + "\n"
	result += "average: " + str(float(genres_correct_total) / float(len(actual_class))) + "\n" + \
	"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< \n"
	return result

def print_accuracy(expected_class, actual_class, genres, features_type, *extra_strings):
	print get_accuracy(expected_class, actual_class,genres,features_type, *extra_strings)

def write_accuracy_to_file(dir_path, expected_class, actual_class, genres, features_type, *extra_strings):
	result = get_accuracy(expected_class, actual_class,genres,features_type, *extra_strings)
	result_file = open(dir_path + "/result.txt", "a")
	result_file.write(result)
	result_file.close()