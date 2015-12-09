import svc as svc
import kNN_algorithm as knn
from itertools import combinations

def run_tests(algorithm, classes_count):
	genres_list = ["blues", "class", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
	genres_combinations = [list(x) for x in combinations(genres_list, classes_count)]
	for genres in genres_combinations:
		algorithm(genres)

run_tests(svc.svm_classification, 4)
run_tests(knn.knn_classification, 4)
