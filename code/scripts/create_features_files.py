import sys
sys.path.append('../')
import track_features as tf

for params in [("../../../music/training", 70), ("../../../music/testing", 30)]:
	path = params[0]
	samples_count = params[1]
	for genre in ["rock", "pop", "class", "jazz"]:
		features_set = tf.get_features(path, samples_count, genre)
		tf.write_features_to_file(path, genre, features_set)
		print "File with features for ", genre, "created"
