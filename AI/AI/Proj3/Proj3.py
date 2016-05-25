# Andrew Maddox
# CMSC 471
# Project 3

# Packages:
# conda install -c https://conda.anaconda.org/menpo opencv3


#import conda.opencv3 as cv3

# Input Picture
# Convert Picture to B/W

def convertPics():

	for i in range(0, 70): 
		fileName = ("%02d"%int(i + 2)) 
		filePath = "/home/andrew/Documents/AI/Proj3/Data/01" + fileName + ".jpg"
		imgTest = cv3.imread(filePath, 0) 
		imgTest= imgTest.flatten() 
		
		datasetTest[0].append(imgTest) 
		datasetTest[1].append(1)

	
	for i in range(0, 70): 
		fileName = ("%02d"%int(i + 2)) 
		filePath = "/home/andrew/Documents/AI/Proj3/Data/02" + fileName + ".jpg"
		imgTest = cv3.imread(filePath, 0) 
		imgTest= imgTest.flatten() 
		
		datasetTest[0].append(imgTest) 
		datasetTest[1].append(1)

	
	for i in range(0, 70): 
		fileName = ("%02d"%int(i + 2)) 
		filePath = "/home/andrew/Documents/AI/Proj3/Data/03" + fileName + ".jpg"
		imgTest = cv3.imread(filePath, 0) 
		imgTest= imgTest.flatten() 
		
		datasetTest[0].append(imgTest) 
		datasetTest[1].append(1)


	
	for i in range(0, 70): 
		fileName = ("%02d"%int(i + 2)) 
		filePath = "/home/andrew/Documents/AI/Proj3/Data/04" + fileName + ".jpg"
		imgTest = cv3.imread(filePath, 0) 
		imgTest= imgTest.flatten() 
		
		datasetTest[0].append(imgTest) 
		datasetTest[1].append(1)

		print("Pictures Flattened...")


def main():

	print("main: " + "\n")



main()
