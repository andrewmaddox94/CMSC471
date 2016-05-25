# Packages:
# git clone git://github.com/numpy/numpy.git numpy


import numpy as np
 


def readFile():

	array = []
	number = 0


#	with open('file.txt') as f:
#		x, y = [int(x) for x in next(f).split()] # read first line
#		array = []
	
#		for line in f: # read rest of lines
#			array.append([int(x) for x in line.split()])

	with open('file.txt') as my_file:
		for line in my_file:
			for word in line.split():
				array.append(word)  


	return array





def main():


	array = readFile()
	print(array)

	np.plot([1,2,3,4])
	np.ylabel('some numbers')
	np.show()



main()





def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters
 
def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu
 
def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))
 
def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)



