from KMeans import KMeans
import numpy as np

def random_sample_generator(lower_bound = 0, upper_bound = 100, n = 10):
		random_sample = []
		for i in range(n):
			random_sample.append([(upper_bound-lower_bound)*np.random.rand()+lower_bound,\
								  (upper_bound-lower_bound)*np.random.rand()+lower_bound])
		return random_sample

points = random_sample_generator(n=100)
k = 5
km = KMeans(points, k)
a = km.kmeans()
km.plot_result(shadeCluster = True)