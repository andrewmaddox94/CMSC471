# Andrew Maddox
# CMSC 471
# Project 2


import sys
import math
import random
import matplotlib.pyplot as pyPlot
import pylab



# function_to_optimize is a pointer to a function that takes two arguments and returns a float

# it is like f(x) = x^2 that you are instering to find the max of
#--------------------------------------------------------------------

def function_to_optimize(x_current = 0, y_current = 0):

	# Initialze variables
	fx = 0.0
	x = x_current 
	y = y_current

	# Calculate function
	fx = x * x * -1

	r = math.sqrt(x*x + y*y)
	fx = (math.sin((x*x) + (3*(y*y))) / (0.1+(r*r))) + (x*x + 5*(y*y)) * (math.exp(1-(r*r))/2)

	return fx	

#--------------------------------------------------------------------


def hill_climb(function_to_optimize, step_size, xmin, xmax, ymin, ymax):

	current_best = 0.0

	# Generate random point to start at
	x = random.uniform(-2.5, 2.5)
	y = random.uniform(-2.5, 2.5)

	# Rename step size
	step = step_size

	# Get starting point for optimization function 
	fx = function_to_optimize(x,y)

	# Create array that stores the values of the x's and y's
	values = []

	tempArray = []

	done = 0
	
	print("test1")

	while(done == 30):

		tempArray = check_moves(x, y, step, xmin, xmax, ymin, ymax)

		print("test2")
		
		#Calculate point on graph
		fx = function_to_optimize(x,y)
		print(fx)

		#store value in list
		values.append(fx)

		#Check if optimal points
		if (current_best == fx):
			current_best = fx
			done = True

		elif (current_best < fx):
			current_best = fx
			step = step_size + step

		else:
			
			if(step == (ymax + step)):
				done = True 

			elif(step == (xmax + step)):			
				done = False
				print("test3")

		done = done + 1
		x = x + step
		y = y + step
		
		
	print("test4")
				
	return current_best

#--------------------------------------------------------------------

def check_moves(x, y, step, xmin, xmax, ymin, ymax):

	myList = []


	if(((x - step >= xmin) and (y - step >= ymin)) and ((x + step <= xmax) and (y + step <= ymax))): 
		myList.append([x,y])

	elif(((x >= xmin) and (y - step >= ymin)) and ((x + step <= xmax) and (y + step <= ymax))): 
		myList.append([x,y])

	elif(((x >= xmin) and (y >= ymin)) and ((x + step <= xmax) and (y + step <= ymax))): 
		myList.append([x,y])

	elif(((x >= xmin) and (y >= ymin)) and ((x <= xmax) and (y + step <= ymax))): 
		myList.append([x,y])

	elif(((x >= xmin) and (y >= ymin)) and ((x <= xmax) and (y <= ymax))): 
		myList.append([x,y])

	elif(((x - step >= xmin) and (y - step >= ymin)) and ((x + step <= xmax) and (y <= ymax))): 
		myList.append([x,y])

	elif(((x - step >= xmin) and (y - step >= ymin)) and ((x <= xmax) and (y <= ymax))): 
		myList.append([x,y])

	elif(((x - step >= xmin) and (y >= ymin)) and ((x <= xmax) and (y <= ymax))): 
		myList.append([x,y])


	return myList

 #if yes, add to possbile list





#def hill_climb_random_restart(function_to_optimize, step_size, num_restarts, xmin, xmax, ymin, ymax):


#def simulated_annealing(function_to_optimize, step_size, max_temp, xmin, xmax, ymin, ymax):


def main():
#	def hill_climb(function_to_optimize, step_size, xmin, xmax, ymin, ymax):

	x = hill_climb(function_to_optimize, 0.5, -2.5, 2.5, -2.5, 2.5)
	


	pyPlot.ylabel('y-axis')
	pyPlot.xlabel('x-axis')
	pyPlot.show()

	print("main: " + "\n")
	print(x)


main()





#	print("\n")
#	for i in range(0, 100):
#
#		x = random.uniform(-2.5, 2.5)
#		y = random.uniform(-2.5, 2.5)
#
#		myList = check_moves(x, y, .1, -2.5, 2.5, -2.5, 2.5) 
#
#		print(myList)
#
#		myList = []

