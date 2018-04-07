import matplotlib.pyplot as plt
import matplotlib
import numpy as np

class KMeans:
	def __init__(self, points, k):
		self.points = points
		self.k = k
		self.set_centroids()
		self.clusters = {}

	def __str__(self):
		string = "Points: " + str(self.points) +\
				 "\nK: " + str(self.k) +\
				 "\nCentroids: " + str(self.centroids)
		return string

	def get_points(self):
		return self.points

	def get_k(self):
		return self.k

	def get_centroids(self):
		return self.centroids

	def get_clusters(self):
		return self.clusters

	def set_centroids(self, centroids_sent = []):
		if(centroids_sent):
			if(len(centroids_sent) != self.k):
				print("Wrong number of centroids for k = " + str(self.k))
			else:
				cdict = {}
				i = 0
				for c in centroids_sent:
					cdict[i] = c
					i = i + 1

				self.centroids = cdict
		else:
			minx = miny = float('inf')
			maxx = maxy = -float('inf')

			for point in self.points:
				minx = min(point[0], minx)
				maxx = max(point[0], maxx)
				miny = min(point[1], miny)
				maxy = max(point[1], maxy)

			divx = float(maxx - minx)/float(self.k)
			divy = float(maxy - miny)/float(self.k)
			centroids = []
			for i in range(self.k):
				centroids.append([minx+i*divx,miny+i*divy])
			cdict = {}
			i = 0
			for c in centroids:
				cdict[i] = c
				i = i + 1

			self.centroids = cdict

	def computeClusters(self):
		clusters = {}
		# Create the empty clusters
		for n in self.centroids:
			clusters[n] = []
		for point in self.points:
			mind = float('inf')
			c = -1
			for ckey, cvalue in self.centroids.items():
				if(mind > self.getDistance(point, cvalue)):
					mind = self.getDistance(point, cvalue)
					c = ckey
			clusters[c].append(point)

		self.clusters = clusters

	def getDistance(self, a, b, mode="euclidean"):
		distance = "Wrong mode"
		if(mode == "euclidean"):
			distance = (a[0] - b[0])**2 + (a[1] - b[1])**2
		return distance

	def computeCentroids(self):
		for key, cluster in self.clusters.items():
			x = 0
			y = 0
			n = 0
			for point in cluster:
				x = x + point[0]
				y = y + point[1]
				n = n + 1
			if(n):
				self.centroids[key] = [float(x)/float(n), float(y)/float(n)]

	def kmeans(self):
		self.computeClusters()
		oldClusters = self.clusters
		iterations = 0
		change = False
		while(not change):
			self.computeCentroids()
			self.computeClusters()
			if(self.clusters == oldClusters):
				change = True
			oldClusters = self.clusters
			iterations = iterations + 1
		return(self.k, self.clusters, self.centroids, iterations)

	def plot_result(self, recompute = False, shadeCluster = False):
		# Recompute the solution if necessary
		if(recompute):
			self.kmeans()

		# Array of colors
		colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:pink', 'tab:orange', 'tab:red', 'tab:purple', 'tab:brown', 'tab:green', 'tab:blue', 'tab:gray', 'tab:olive', 'tab:cyan']

		# Size and opacity of the instance points in scatter
		si = 40
		ai = 0.6

		# Size and opacity of the centroid points in scatter
		sc = 50
		ac = 1
		if(shadeCluster):
			sc = 75000/self.k
			ac = 0.1

		# Iterate through clusters and centroids
		for i in range(self.k):
			# X and Y coordinates of the instances
			pointsx = np.array([point[0] for point in self.clusters[i]])
			pointsy = np.array([point[1] for point in self.clusters[i]])

			plt.scatter(pointsx, pointsy, si, c=colors[i%17], alpha=ai, marker="s",
			            label="Cluster " + str(i))

			# X and Y coordinates of the centroids
			centroidx = np.array([self.centroids[i][0]])
			centroidy = np.array([self.centroids[i][1]])

			plt.scatter(centroidx, centroidy, sc, c=colors[i%17], alpha=ac, marker="o")

		# Labels
		plt.title("K-Means (K=" + str(self.k) + ")")
		plt.xlabel("X")
		plt.ylabel("Y")
		plt.legend(loc='center left',  bbox_to_anchor=(1, 0.5))
		# If the axes want to be set
		# Y-axis lower bound
		#plt.ylim(ymin=0)
		# Y-axis upper bound
		#plt.ylim(ymax=0)
		# X-axis lower bound
		#plt.xlim(xmin=0)
		# X-axis upper bound
		#plt.xlim(xmax=0)
		plt.show()