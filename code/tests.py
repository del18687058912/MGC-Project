import os
import svc as svc
import kNN_algorithm as knn
from itertools import combinations

def run_tests(algorithm, classes_count, features_type):
	genres_list = ["blues", "class", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
	genres_combinations = [list(x) for x in combinations(genres_list, classes_count)]
	for genres in genres_combinations:
		algorithm(genres, features_type)

result_path = "../../music/result.txt"
if (os.path.isfile(result_path)):
	os.remove(result_path)
	
run_tests(svc.svm_classification, 4, "mfcc")
run_tests(knn.knn_classification, 4, "mfcc")
